import json
import os
import sys
import math

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open (filepath, 'r') as reader:
        return json.load(reader)


def get_biggest_bar(reader):
    return max( reader, key=lambda item: item['SeatsCount'])


def get_smallest_bar(reader):
    return min( reader, key = lambda item: item['SeatsCount'])

def get_closest_bar(reader, longitude, latitude):
    return min(reader, key = lambda item: (item['geoData']['coordinates'][0] - longitude)**2 + (item['geoData']['coordinates'][1]-latitude)**2)


if __name__ == '__main__':
    if len(sys.argv)>1:
        filepath = sys.argv[1]
        reader = load_data(filepath)
        biggest_bar = get_biggest_bar(reader)
        print('The biggest bar \n', json.dumps(biggest_bar, indent = 4, ensure_ascii=False, sort_keys = True))
        smallest_bar = get_smallest_bar(reader)
        print('The smallest bar \n', json.dumps(smallest_bar, indent = 4, ensure_ascii=False, sort_keys = True))
        print('Please enter your GeoData')
        latitude = float(input('enter the latitude '))
        longitude = float(input('enter the longitude '))
        closest_bar = get_closest_bar(reader,longitude,latitude)
        print('The closest bar \n', json.dumps(closest_bar, indent = 4, ensure_ascii = False, sort_keys = True))
    else:
        print("Please, enter the filepath")
