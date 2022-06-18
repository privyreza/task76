from django.db import models
from django.contrib import auth

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(auth.get_user_model())
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()