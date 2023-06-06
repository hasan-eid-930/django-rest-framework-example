from django.contrib import admin
from .models import Book, Rating

# Register your models here.



class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'stars']
    list_filter = ['book', 'user']
    

class BookAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'description','slug']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']

admin.site.register(Book, BookAdmin)
admin.site.register(Rating, RatingAdmin)