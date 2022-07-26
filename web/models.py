from django.db import models

# Create your models here.

class Service_Category(models.Model):
    Service_Category_Name = models.CharField(max_length = 100)

class Services(models.Model):
    Thumbnail = models.ImageField(upload_to ='Service_Thumbnail')
    Service_Title = models.CharField(max_length = 200)
    Description = models.TextField()
    Service_Category = models.ForeignKey(Service_Category, on_delete=models.CASCADE)

