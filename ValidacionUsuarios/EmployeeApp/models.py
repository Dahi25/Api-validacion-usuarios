from msilib.schema import Class
from django.db import models

# Create your models here.


class Nombres(models.Model):
    Nombre=models.CharField(max_length=100) # Return type inferred as None, considered as typed method
        