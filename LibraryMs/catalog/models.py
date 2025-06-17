import uuid

from django.db import models
from django.contrib.auth.models import User
from user.models import Author
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    GENRE_CHOICES = (
        ("R","ROMANCE"),
        ("D","COMEDY"),
        ("P","POLITICS"),
        ("F","FINANCE"),
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="F", unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
        ("A","AVAILABLE"),
        ("B","BORROWED"),
        ("M","MAINTENANCE"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default="A", unique=True)
    release_date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Language(models.Model):
    LANGUAGE_CHOICES = (
        ("EN", "English"),
        ("FR", "French"),
        ("ES", "Spanish"),
        ("PT", "Portuguese"),
        ("IT", "Italian"),
    )
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="EN", unique=True)


