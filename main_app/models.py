from django.db import models
from django.urls import reverse

# Create your models here.
class Crypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crypto_id': self.id})