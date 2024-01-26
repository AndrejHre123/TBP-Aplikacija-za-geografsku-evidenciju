from django.contrib.gis.db import models

# Create your models here.
class Shop(models.Model):
    ime = models.CharField(max_length=100)
    lokacija = models.PointField()
    adresa = models.CharField(max_length=100)
    grad = models.CharField(max_length=50)
    radno_vrijeme = models.TextField()
    web = models.URLField()