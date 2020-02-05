from django.db import models

# Create your models here.
class Hero(models.Model):
    # id is auto generated primary key
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    # add auto_now_add to set birthday to creation date
    birthday = models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name