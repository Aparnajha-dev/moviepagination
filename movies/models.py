from django.db import models

class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.movie_name
