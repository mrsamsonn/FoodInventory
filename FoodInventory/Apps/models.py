from django.db import models

class Product(models.Model):
    upc = models.CharField(max_length=100, unique=True)
    ean = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.title