from rest_framework import serializers
from byuier.news import models
from datetime import datetime
from django.utils.timesince import timesince


#
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField(default=True)
#     created = serializers.DateTimeField(read_only=True)
#     updated = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_date):
#         print(validated_date)
#         return models.Article.objects.create(**validated_date)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         # instance.created = validated_data.get('created', instance.created)
#         # instance.updated = validated_data.get('updated', instance.updated)
#         instance.save()
#         return instance
#
#     # Object Level Validation
#     def validate(self, data):
#         """
#         Check the title and description are different
#         :param data:
#         :return:
#         """
#         if data['title'] == data['description']:
#             raise serializers.ValidationError('Title and Description must be different.')
#         return data
#
#     # Field level Validation
#     def validate_title(self, value):
#         if len(value) < 10:
#             raise serializers.ValidationError('Field title must be more than 20 characters long.')
#         return value
