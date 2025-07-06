from django.contrib import admin
from django.contrib import admin
from .models import Book, Review, BorrowRequest

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BorrowRequest)

# Register your models here.
