from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
        return self.title
