from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    published_date = models.IntegerField()
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.title
