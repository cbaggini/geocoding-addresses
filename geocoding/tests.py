from django.test import TestCase

from itertools import islice
import csv

from .models import Address

# csv file with addresses and coordinates for testing is not included in GitHub repo.

class AddressTestCase(TestCase):

    def test_correct_addresses(self):
        with open('geocoding/test_addresses.csv') as test_file:
            csv_reader = csv.reader(test_file, delimiter=',')
            next(csv_reader)
            # selects only 10 addresses to test; can be changed
            for row in list(csv_reader)[50:80]:
                a = Address(city=row[4], number=row[2], street=row[3], postal_code=row[7],address_type='shipping', country=' ')
                a.save()
                geocoded_address = Address.objects.get(street=row[3],number=row[2],city=row[4])
                coords = row[10].strip('][').split(', ') 
                self.assertEqual(geocoded_address.status,'Success')
                # rounded to 2 decimals - that's an error of just over 1 km
                self.assertEqual(round(geocoded_address.lon,2), round(float(coords[0]),2))
                self.assertEqual(round(geocoded_address.lat,2), round(float(coords[1]),2))

    def test_invalid_API_call(self):
        a = Address(city='fghsfr', number='fgwef', street='fhgvbaijow', postal_code='gu',address_type='shipping', country=' ')
        a.save()
        geocoded_address = Address.objects.get(street='fhgvbaijow')
        self.assertEqual(geocoded_address.status,'No address found')

    def test_invalid_address(self):
        a = Address(city='Plymouth', number='24', street='Christchurch Avenue', 
            postal_code=' ',address_type='shipping', country=' ')
        a.save()
        geocoded_address = Address.objects.get(street='Christchurch Avenue')
        self.assertEqual(geocoded_address.status,'More than one address')