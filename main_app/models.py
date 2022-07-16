from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Crypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    date = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crypto_id': self.id})

