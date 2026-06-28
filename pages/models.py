from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
