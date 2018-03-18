import folium
import pandas


data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
	if elevation < 1000:
		return 'green'
	elif 1000 <= elevation < 3000:
		return 'orange'
	else:
		return 'red' 


#map = folium.Map(location=[38.56, -99.09], zoom_start=6)
map = folium.Map(location=[38.56, -99.09], zoom_start=6, tiles="Mapbox Bright")

# A Child layer created for placing Volcano makers 
#   and added as a separate feature group
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
	fgv.add_child(folium.CircleMarker(location=[lt, ln],
					radius=6, 
					#Or, popup=folium.Popup(str(el), parse_html=true))
					popup=str(el)+"m", 
					fill_color=color_producer(el),
					color='grey',
					fill=True,
					fill_opacity=0.7))

# Second Child layer created for placing Population marked from multipolygons
#   and added as a separate feature group
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
	style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#add both childs to base map
map.add_child(fgv)
map.add_child(fgp)

# add a layer control for selecting/deselecting the controls
map.add_child(folium.LayerControl())

map.save("GeoMap-VolcanoPopulation.html")