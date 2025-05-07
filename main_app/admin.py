from django.contrib import admin
from .models import Date, Food

# Register your models here.

admin.site.register([Date, Food]) #or [Date]