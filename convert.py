import os
import subprocess

cod =[
		#{'iso3':'BDI', 'iso2':'BI', 'use':'BDI', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'MLI', 'iso2':'ML', 'use':'ML', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'NGA', 'iso2':'NG', 'use':'NG', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'CAF', 'iso2':'CF', 'use':'CF', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'BFA', 'iso2':'BF', 'use':'BF', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'CIV', 'iso2':'CI', 'use':'CI', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'COD', 'iso2':'CD', 'use':'CD', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'COL', 'iso2':'CO', 'use':'CO', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'GIN', 'iso2':'GN', 'use':'GN', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'SLE', 'iso2':'SL', 'use':'SL', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'AGO', 'iso2':'AO', 'use':'AO', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'BGD', 'iso2':'BD', 'use':'BD', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'CMR', 'iso2':'CM', 'use':'CM', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'EGY', 'iso2':'EG', 'use':'EG', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'GTM', 'iso2':'GT', 'use':'GT', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'HND', 'iso2':'HD', 'use':'HD', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'HTI', 'iso2':'HT', 'use':'HT', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'IRQ', 'iso2':'IQ', 'use':'IQ', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'KDN', 'iso2':'KD', 'use':'KDN', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'KEN', 'iso2':'KE', 'use':'KE', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'KGZ', 'iso2':'KG', 'use':'KG', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'KHM', 'iso2':'KH', 'use':'KH', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'LBN', 'iso2':'LB', 'use':'LB', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		{'iso3':'MOZ', 'iso2':'MZ', 'use':'MZ', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'MRT', 'iso2':'MT', 'use':'MT', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'MWI', 'iso2':'MW', 'use':'MW', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'NER', 'iso2':'NE', 'use':'NE', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'NPL', 'iso2':'NP', 'use':'NP', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'PAK', 'iso2':'PK', 'use':'PK', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'PSE', 'iso2':'PS', 'use':'PS', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'SDN', 'iso2':'SD', 'use':'SD', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'SOM', 'iso2':'SO', 'use':'SO', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'SSD', 'iso2':'SS', 'use':'SS', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'TCD', 'iso2':'TD', 'use':'TD', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':1,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'UKR', 'iso2':'UA', 'use':'UA', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'VEN', 'iso2':'VE', 'use':'VEN', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'VUT', 'iso2':'VU', 'use':'VU', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'YEM', 'iso2':'YE', 'use':'YE', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
		#{'iso3':'ZWE', 'iso2':'ZW', 'use':'ZW', 'url':'https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/{{country}}_pcode/MapServer/{{level}}/query?where=1%3D1&outFields=*&f=geojson','adjustment':0,'code_att':'admin{{level}}Pcode','name_att':'admin{{level}}RefName'},
	]

for country in cod:
	print country
	for level in range(1,4):
		print level
		geojson = 'geoms/geojson/'+country['iso3']+'/'+str(level)+'/geom.geojson'
		topojson = 'geoms/topojson/'+country['iso3']+'/'+str(level)+'/geom.json'
		if not os.path.exists('geoms/topojson/'+country['iso3']+'/'+str(level)):
			os.makedirs('geoms/topojson/'+country['iso3']+'/'+str(level))
		prop1 = country['code_att'].replace('{{level}}',str(level))
		prop2 = country['name_att'].replace('{{level}}',str(level))
		print subprocess.check_output(['topojson',geojson,'-o',topojson,'-p',prop1+','+prop2])