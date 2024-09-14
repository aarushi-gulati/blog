from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200000)
    published_on = models.DateTimeField('Date Published')