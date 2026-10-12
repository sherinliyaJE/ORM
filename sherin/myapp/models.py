from django.db import models
from django.contrib import admin 
class service_DB(models.Model):
    Vehicle_No=models.CharField(primary_key=True)
    vehicle_model=models.CharField()
    user_Name=models.CharField(max_length=20)
    Number=models.IntegerField()
    Email=models.EmailField()
    Address=models.TextField()
    Date=models.DateField()
class service_DBAdmin(admin.ModelAdmin):
    list_display=["Vehicle_No","vehicle_model","user_Name","Number","Email","Address","Date"]
