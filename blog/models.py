from django.db import models

class Posting(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='', null=True, blank=True)