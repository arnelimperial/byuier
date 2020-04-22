from django.db import models


class Journalist(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "ID: {} - {} {}".format(self.id, self.first_name, self.last_name)


class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    location = models.CharField(max_length=255)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} - {}".format(self.author, self.title)

    def __str__(self):
        return "{} - {}".format(self.author, self.title)



