from django.forms import ModelForm
from .models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['address_type', 'number', 'street', 'city', 'postal_code', 'country']
