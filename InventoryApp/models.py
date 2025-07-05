from django.db import models

# Create your models here.
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    barcode = models.IntegerField(unique=True)