# models.py
from django.db import models

class RadarEntry(models.Model):
    label = models.CharField(max_length=100)
    quadrant = models.IntegerField()
    ring = models.IntegerField()
    moved = models.IntegerField()
    
    def __str__(self):
        return self.label
