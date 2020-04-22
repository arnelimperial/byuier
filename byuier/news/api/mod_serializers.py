from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from byuier.news import models
from datetime import datetime
from django.utils.timesince import timesince


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    # return string repr of the foreign key
    author = serializers.StringRelatedField()

    # return json repr of the foreign key
    # author = JournalistSerializer(read_only=True)

    class Meta:
        model = models.Article
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=models.Article.objects.all(),
                fields=['title', 'description']

            )

        ]

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Field title must be more than 20 characters long.')
        return value


class JournalistSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article-detail'
    )

    class Meta:
        model = models.Journalist
        fields = '__all__'
