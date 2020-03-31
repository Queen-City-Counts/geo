import folium, os

neighborhoods = os.path.join('data','Neighborhoods.geojson')
nbhd = folium.Map([42.886416, -78.878177], title='OpenStreetMap', zoom_start = 10)
folium.Choropleth(geo_data = neighborhoods, fill_color='blue', fill_opacity = 0.7, line_weight = 2).add_to(nbhd)
nbhd.save('nbhd.html')


##nbhdname
