from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.username
# Create your models here.
