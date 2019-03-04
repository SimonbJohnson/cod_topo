import os
import subprocess

cod =[
		{'iso3':'BDI', 'iso2':'BI', 'use':'BDI', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'MLI', 'iso2':'ML', 'use':'ML', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'NGA', 'iso2':'NG', 'use':'NG', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'CAF', 'iso2':'CF', 'use':'CF', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'BFA', 'iso2':'BF', 'use':'BF', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'CIV', 'iso2':'CI', 'use':'CI', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'COD', 'iso2':'CD', 'use':'CD', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'COL', 'iso2':'CO', 'use':'CO', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'GIN', 'iso2':'GN', 'use':'GN', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'SLE', 'iso2':'SL', 'use':'SL', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},

	]

for country in cod:
	print country
	for level in range(1,3):
		print level
		geojson = 'geoms/geojson/'+country['iso3']+'/'+str(level)+'/geom.geojson'
		topojson = 'geoms/topojson/'+country['iso3']+'/'+str(level)+'/geom.json'
		if not os.path.exists('geoms/topojson/'+country['iso3']+'/'+str(level)):
			os.makedirs('geoms/topojson/'+country['iso3']+'/'+str(level))
		print subprocess.check_output(['topojson',geojson,'-o',topojson,'-p'])