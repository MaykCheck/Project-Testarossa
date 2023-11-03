from django.db import models

# Create your models here.

class Car(models.Model):

    def __str__(self):
        return self.CarName
    
    CarName = models.CharField(max_length=200)
    CarDesc = models.CharField(max_length=200)
    CarPrice = models.BigIntegerField()
    CarImage = models.CharField(max_length=500, default="https://shop.roadster.com/assets/car-placeholder-652ae305f4b4afc9eb5f2d976fa0f77979069acb686b0a16fcc062e210367660.png")