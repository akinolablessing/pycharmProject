from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = ""
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    language = ""

    def __str__(self):
        return self.title

class Language(models.Model):
    LANGUAGE_CHOICES = (
        ("en", "English"),
        ("fr", "French"),
        ("es", "Spanish"),
        ("pt", "Portuguese"),
        ("it", "Italian"),
    )
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)

class Genre(models.Model):
    GENRE_CHOICES = (
        ("R","ROMANCE"),
        ("D","COMEDY"),
        ("P","POLITICS"),
        ("F","FINANCE"),
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="F")

    def __str__(self):
        return self.name