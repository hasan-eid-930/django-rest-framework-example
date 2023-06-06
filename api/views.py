from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Book, Rating
from .serializers import BookSerializer, RatingSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
 
def test(request):
    for b in Book.objects.all():
        b.delete()
    return HttpResponse('hello')