from django.db import models
# make mmigrations - make changes and save them ina file 
#migrste - apply the changes made by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=125)
    phone = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name