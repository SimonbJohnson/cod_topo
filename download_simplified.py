import os
import subprocess
import csv
import json
import urllib

links = []

i=0
with open('simplified_geoms.csv','rU') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		if i>0:
			print row[3]
			country = row[3].split('_')[1]
			level = row[3].split('_')[2][5]
			print level
			print country
			if int(level)>0:
				print "downloading"
				newURL = row[4]
				if not os.path.exists('geoms_simp/geojson/'+country+'/'+str(level)):
					os.makedirs('geoms_simp/geojson/'+country+'/'+str(level))
				file = urllib.URLopener()
				try:
					file.retrieve(newURL, 'geoms_simp/geojson/'+country+'/'+str(level)+'/geom.geojson')
				except:
					print "Could not download "+country+" - level "+str(level)
		i=i+1