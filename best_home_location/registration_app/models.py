
# Create your models here.

from django.db import models

class Registration(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    property_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.property_name}"
