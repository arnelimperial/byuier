from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    location = models.CharField(max_length=255)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.author, self.title)



