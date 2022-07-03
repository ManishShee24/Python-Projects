import phonenumbers
from phonenumbers import geocoder, carrier

number = '+918583815550'

# get location provider
sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber, 'en')
print(yourLocation)

# get service provider
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

Key = "ebdf78271cb14e50b66c02e79809d037"

from opencage.geocoder import OpenCageGeocode
GeoCoder = OpenCageGeocode(Key)
query = str(yourLocation)
result = GeoCoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)