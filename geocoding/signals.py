from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse

from geopy.geocoders import GoogleV3

from .models import Address
from staiy import params

@receiver(post_save, sender=Address)
def geocode(instance, **kwargs):
    geolocator = GoogleV3(api_key=params.GOOGLE_API_KEY)
    location = geolocator.geocode(instance,exactly_one=False)
    if len(location) == 1:
        # Geographical Coordinate system is hard-coded because Google Maps API will always use that. 
        # Will need to be changed if a different service is used
        my_data_dict = {'status':'Success', 'lat': location[0].latitude, 'lon': location[0].longitude, 'geom_srid': 4326}
    elif len(location) > 1:
        my_data_dict = {'status':'More than one address'}
    else:
        my_data_dict = {'status':'No address found'}
    Address.objects.filter(pk=instance.pk).update(**my_data_dict)
    return JsonResponse(my_data_dict)