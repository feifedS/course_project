from django.db import models

# Create your models here.
class Weather(models.Model):
    coord = models.CharField("Координаты", max_length=255)
