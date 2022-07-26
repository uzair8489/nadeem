from django.contrib import admin
from .models import *
# Register your models here.

class servicecategory_data(admin.ModelAdmin):
    list_display = ['Service_Category_Name']

admin.site.register(Service_Category, servicecategory_data)