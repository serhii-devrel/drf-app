from rest_framework import serializers

from .models import Book, Author, Category


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=128)
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
