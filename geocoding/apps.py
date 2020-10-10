from django.apps import AppConfig


class GeocodingConfig(AppConfig):
    name = 'geocoding'
    label = 'geocoding'
    def ready(self):
        import geocoding.signals
