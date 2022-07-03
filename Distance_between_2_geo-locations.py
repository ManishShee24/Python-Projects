from geopy.geocoders import Nominatim
from geopy import distance

a = Nominatim(user_agent = "Fun with data science")
place_1 = "Kolkata"
place_2 = "Kerala"

destination_1 = a.geocode(place_1)
destination_2 = a.geocode(place_2)

lat_1, long_1 = (destination_1.latitude), (destination_1.longitude)
lat_2, long_2 = (destination_2.latitude), (destination_2.longitude)

length_1 = (lat_1, long_1)
length_2 = (lat_2, long_2)

print("distance between",place_1,"and",place_2,"is:",distance.distance(length_1, length_2))