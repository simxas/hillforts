import folium
import pandas
import os

data_frame = pandas.read_csv('Hillforts.csv')
subdirectory = "htmls"

def view_all_forts():
    all_data = data_frame['Name']
    return all_data

def view_all_regions():
    # removes all duplicates
    df = data_frame.drop_duplicates('Region')
    regions = df['Region']
    return regions

def search_by_name(name=''):
    hillfort = data_frame[data_frame['Name'] == name]
    return hillfort

def search_by_region(name=''):
    str(name)
    hillfort = data_frame[data_frame['Region'] == name]
    return hillfort

def generate_by_selection(name):
    hillfort = data_frame[data_frame['Name'] == name]
    lat = float(hillfort['latitude'])
    lon = float(hillfort['longitude'])
    map = folium.Map(location=[lat, lon], zoom_start=12)
    map.simple_marker(location=[lat, lon], popup=name)
    map.create_map(path=os.path.join(subdirectory, '{0}.html'.format(name)))

def generate_by_region(region):
    hillforts = data_frame[data_frame['Region'] == region]
    map = folium.Map(location=[hillforts.iloc[0]['latitude'], hillforts.iloc[0]['longitude']], zoom_start=10)
    for lat, lon, name in zip(hillforts['latitude'], hillforts['longitude'], hillforts['Name']):
        map.simple_marker(location=[lat, lon], popup=name)
    map.create_map(path=os.path.join(subdirectory, '{0}.html'.format(region)))
