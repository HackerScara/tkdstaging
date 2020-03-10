from django.db import models

class stage(models.Model):
    ring = models.CharField(max_length=2)
    age = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.ring
