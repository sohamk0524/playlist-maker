from django.db import models

# Create your models here.

class Song(models.Model):
	name = models.CharField(max_length = 50)
	genre = models.CharField(max_length = 25)
	cover = models.ImageField(upload_to = 'uploads/songs/', default='default')
	

