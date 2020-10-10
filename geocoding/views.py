from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets   
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer, HTMLFormRenderer
from rest_framework.response import Response

import folium

from .serializers import AddressSerializer      
from .models import Address  
from .forms import AddressForm                  

# this is the view for the API interface
class AddressView(viewsets.ModelViewSet):       
  serializer_class = AddressSerializer 
  queryset = Address.objects.all()  

  def update(self, request, *args, **kwargs):
    partial = True
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    return Response(serializer.data)

# this is the view for the main page with form and map
class main(View):
  form_class = AddressForm
  template_name = 'geocoding/main.html'
  def get(self, request):
    form = self.form_class()
    return render(request, self.template_name, {'form': form})
  
  def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            entry = self.form_class(request.POST)
            address = entry.save()
            geocoded_address = Address.objects.get(pk=address.pk)
            form = self.form_class()
            context = {'form': form, 'geocoded_address': geocoded_address}
            if geocoded_address.lon:
              m = folium.Map(location=[geocoded_address.lat, geocoded_address.lon],zoom_start=15)
              folium.Marker([geocoded_address.lat, geocoded_address.lon]).add_to(m)
              address_map=m._repr_html_()
              context['address_map'] = address_map
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'form': form})