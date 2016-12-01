import folium
import pandas

data_frame = pandas.read_csv('Hillforts.csv')

map = folium.Map(location=[55.063916666666664, 22.74475], zoom_start=10)

for lat, lon, name in zip(data_frame['latitude'], data_frame['longitude'], data_frame['Name']):
    map.simple_marker(location=[lat, lon], popup=name)

map.create_map(path='hillforts.html')

# For tests
# map = folium.Map(location=[54.40530555555556, 23.883111111111113], zoom_start=10)
#
# map.simple_marker(location=[54.40530555555556, 23.883111111111113], popup='test')
#
# map.create_map(path='test.html')
