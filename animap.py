import folium
import pandas as pd
import numpy as np
from folium import plugins
pd.set_option('display.max_columns', None) 

df = pd.read_csv('/home/dan/Python/QueenCityCounts/maps/data/Crime_Incidents.csv', dtype=str)
df = df[['incident_datetime','latitude','longitude','incident_type_primary']]
df['incident_datetime'] = pd.to_datetime(df['incident_datetime'])
df['year'] = df['incident_datetime'].apply(lambda x: x.year)
df['week'] = df['incident_datetime'].apply(lambda x: x.week)
df.sort_values(by=['year','week'], inplace=True)
df = df.loc[(df['year'] >= 2010) & ((df['incident_type_primary'] == 'RAPE') | (df['incident_type_primary'] == 'SEXUAL ABUSE'))].reset_index()
df['latlng'] = list(zip(df['latitude'],df['longitude']))

data = df[['week', 'latlng']]
data = data[data['week']!=53.0]
data['latlng'] = data['latlng'].apply(list)
data = data.groupby('week')['latlng'].apply(list).reset_index()


heatmap_time_data = data['latlng'].to_list()

# dates
heatmap_time_dates = list(range(1,len(heatmap_time_data)+1))
# map
map_heatmap_time = folium.Map([42.9362, -78.8433], zoom_start=12)
# heatmap plugin
heatmap_time_plugin = plugins.HeatMapWithTime(heatmap_time_data, index=heatmap_time_dates)
full_screen_plugin = plugins.Fullscreen(position='topright')
# add heatmap plugin to map
heatmap_time_plugin.add_to(map_heatmap_time)
full_screen_plugin .add_to(map_heatmap_time)
# display map
map_heatmap_time.save('map.html')


# Read in the file
with open('map.html', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('https://rawcdn.githack.com/socib/Leaflet.TimeDimension/master/dist/leaflet.timedimension.min.js', 'https://cdn.jsdelivr.net/npm/leaflet-timedimension@1.1.0/dist/leaflet.timedimension.min.js')

# Write the file out again
with open('map.html', 'w') as file:
  file.write(filedata)

#https://rawcdn.githack.com/socib/Leaflet.TimeDimension/master/dist/leaflet.timedimension.min.js

#https://cdn.jsdelivr.net/npm/leaflet-timedimension@1.1.0/dist/leaflet.timedimension.min.js
