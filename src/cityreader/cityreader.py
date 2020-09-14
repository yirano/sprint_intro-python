# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.


def cityreader():
    # TODO Implement the functionality to read from the 'cities.csv' file
    # Ensure that the lat and lon valuse are all floats
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open('cities.csv', newline='') as csv_file:
        read = csv.reader(csv_file, delimiter=',')
        cities = [City(r[0], float(r[3]), float(r[4]))
                  for r in read if r[0] != 'city']

        return cities


cities = cityreader()

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

# upper = input('Input lat and lon for upper-left corner separated by a comma: ')
# lower = input(
#     'Input lat and lon for lower-right corner separated by a comma: ')

upper = '45, -100'
lower = '32, -120'


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    upper_lat = 0
    upper_lon = 0
    lower_lat = 0
    lower_lon = 0
    if lat1 > lat2:
        upper_lat = lat1
        upper_lon = lon1
        lower_lat = lat2
        lower_lon = lon2
    else:
        upper_lat = lat2
        upper_lon = lon2
        lower_lat = lat1
        lower_lon = lon1

    within = [city for city in cities if city.lat < upper_lat and city.lon <
              upper_lon and city.lat > lower_lat and city.lon > lower_lon]

    # Go through each city and check to see if it falls within
    # the specified coordinates.

    return within


def normalize_input(inp_1, inp_2):
    inps = inp_1.split(', ') + inp_2.split(', ')
    return [float(inp) for inp in inps]


p = normalize_input(upper, lower)
# print(p)
filtered_cities = cityreader_stretch(p[0], p[1], p[2], p[3], cities)

for city in filtered_cities:
    print(city)
