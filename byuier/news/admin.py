from django.contrib import admin
from . import models

newsModels = [models.Article, models.Journalist]
admin.site.register(newsModels)
