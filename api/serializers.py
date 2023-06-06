from rest_framework import serializers
from .models import Book, Rating




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['slug', 'title', 'description']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'book']