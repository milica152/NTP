from django.db import models


# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField
    dod = models.DateField(null=True)
    image = models.CharField(max_length=1000)
    children = models.ManyToManyField("self")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
