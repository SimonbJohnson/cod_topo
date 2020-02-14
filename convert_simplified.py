import os
import subprocess
import csv
import json

links = []

with open('itos_service.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		if row[1]=='MapServer':
			if row[2]=='pcode':
				if len(row[4])==6 and row[4]!='Admin0':
					links.append([row[0],row[4][5:],row[3]])

listOfAtts = ['admin{level}RefName','Admin{level}Name','admin{level}Name_en','ADM{level}_EN','admin{level}Name_fr','admin{level}Name_es','admin{level}Name_pt','admin{level}Name_ar']
for link in links:
	country = link[0]
	level = link[1]
	name_att = 'admin'+level+'Name'
	code_att = 'admin'+level+'Pcode'
	geojson = 'geoms_simp/geojson/'+country+'/'+str(level)+'/geom.geojson'
	topojson = 'geoms_simp/topojson/'+country+'/'+str(level)+'/geom.json'
	print country + ' - ' + level
	try:
		with open(geojson) as json_file:
			geojsonFile = json.load(json_file)
			feature = geojsonFile['features'][0]['properties']
			foundAtt = None
			for att in listOfAtts:
				if foundAtt == None:
					attlevel = att.replace('{level}',level)
					if attlevel in feature:
						if feature[attlevel] != None:
							foundAtt = attlevel
			if foundAtt == None:
				print feature
			else:
				print foundAtt
				for feature in geojsonFile['features']:
					feature['properties'][name_att] = feature['properties'][foundAtt]
					del feature['properties'][foundAtt]

			newFile = 'geoms_simp/geojson/'+country+'/'+str(level)+'/geom.geojson'

			with open(newFile, 'w') as outfile:
				json.dump(geojsonFile, outfile)

		if not os.path.exists('geoms_simp/topojson/'+country+'/'+str(level)):
		 	os.makedirs('geoms_simp/topojson/'+country+'/'+str(level))
		print subprocess.check_output(['topojson',newFile,'-o',topojson,'-p',name_att+','+code_att])

	except Exception as e:
		print "error"
		print e
		