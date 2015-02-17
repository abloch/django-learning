from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    