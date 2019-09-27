import os
import urllib
import csv

links = []
url = 'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{layer}}/query?where=1%3D1&outFields=*&f=geojson'

with open('itos_service.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
    	if row[1]=='MapServer':
    		if row[2]=='pcode':
	    		if len(row[4])==6 and row[4]!='Admin0':
	    			links.append([row[0],row[4][5:],row[3]])

print links

for row in links:
	country = row[0]
	layer = row[2]
	level = row[1]
	if country>'WCA' and int(layer)>-1:
		newURL = url.replace('{{country}}',country).replace('{{layer}}',layer)
		print newURL
		if not os.path.exists('geoms/geojson/'+country+'/'+str(level)):
			os.makedirs('geoms/geojson/'+country+'/'+str(level))
		file = urllib.URLopener()
		file.retrieve(newURL, 'geoms/geojson/'+country+'/'+str(level)+'/geom.geojson')