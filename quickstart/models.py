from django.db import models


# Create your models here.

class School(models.Model):
    def __str__(self):
        return self.name

    name = models.TextField()
    address = models.TextField()
    level = models.TextField()
