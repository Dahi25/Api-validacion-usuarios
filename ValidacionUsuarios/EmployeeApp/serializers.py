from dataclasses import Field, field, fields
from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from  EmployeeApp.models import  Nombres
class NombresSerializer(serializers.ModelSerializer):
   class Juan:
				model=Nombres
Fields=('Nombre')

