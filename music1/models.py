from multiprocessing.forkserver import MAXFDS_TO_SEND
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    F_name=models.CharField
    L_name=models.CharField
    Age=models.IntegerField
    Art_id=models.CharField
class Song(models.Model):
    Title=models.CharField
    Datereleased=models.DateField
    Likes=models.IntegerField
    Art_id=models.CharField
class Lyrics(models.Model):
    Content=models.CharField
    Song_id=models.CharField
    Art_id=models.CharField

