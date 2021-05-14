from django.db import models

# Create your models here.
'''
class ServiceData(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="pic")
'''


class ServiceData(models.Model):
    head = models.CharField(max_length=50)
    des = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="pic")
