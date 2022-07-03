from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=125)
    phone = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    desc = models.TextField()
    date = models.DateField()