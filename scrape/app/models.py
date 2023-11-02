from django.db import models

# Create your models here.
class Scrapeimage(models.Model):
    url = models.URLField(max_length=200)
    name_of_image = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True) 