from django.db import models

# Create your models here.
class Island(models.Model):
    name = ''
    beaches = ''

class Beach(models.Model):
    name = ''
    island = ''
    difficulty = ''
    posts = ''

class Post(model):
    title = ''
    body = ''
    image = ''
    author = ''