from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Family(models.Model):
    name = CharField(max_length=100)

class Animal(models.Model):
    name = CharField(max_length=50)
    legs = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    height = models.SmallIntegerField()
    Speed = models.SmallIntegerField()
    family = ForeignKey(Family, models.CASCADE)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name
