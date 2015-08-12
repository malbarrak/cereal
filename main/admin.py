from django.contrib import admin

from main.models import Cereal, Manufacturer, Nutrition_Facts
# Register your models here.

admin.site.register(Cereal)
admin.site.register(Manufacturer)
admin.site.register(Nutrition_Facts)
