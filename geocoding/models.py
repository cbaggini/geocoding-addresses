from django.db.models import CharField, ForeignKey, FloatField, Model, CASCADE, PROTECT
from django.contrib.gis.geos import Point
from django.db import connection 

# This imports the complete projection list 
SpatialRefSys = connection.ops.spatial_ref_sys()  

class Address(Model):
    address_type = CharField(
        max_length=8,
        choices=[
            ("shipping", "Shipping"),
            ("billing", "Billing"),
        ]
    )
    city = CharField(max_length=200)
    number = CharField(max_length=200)
    street = CharField(max_length=200)
    # country = ForeignKey(
    #     "Country",
    #     on_delete=CASCADE,
    # )
    country = CharField(max_length=200)
    postal_code = CharField(max_length=50)
    geom_srid = ForeignKey(SpatialRefSys, on_delete=PROTECT, blank=True, null=True)
    geometry = Point()
    lat = FloatField(blank=True, null=True)
    lon = FloatField(blank=True, null=True)
    status = CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.number} {self.street}, {self.postal_code} {self.city}, {self.country}"

