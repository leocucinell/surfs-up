from django.db import models
from django.conf import settings

# Create your models here.
class Island(models.Model):
    name = models.CharField(max_length=350)
    #beaches = ''

class Beach(models.Model):
    name = models.CharField(max_length=350)
    island = models.ForeignKey(
        'Island',
        on_delete=models.CASCADE,
    )
    difficulty = models.BigIntegerField()
    #posts = ''

class Post(models.Model):
    title = models.CharField(max_length=350)
    body = models.TextField()
    image = models.FileField(blank=True, null=True) #TODO: Decide where to upload this later
    beach = models.ForeignKey(
        'Beach',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )