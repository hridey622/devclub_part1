from django.contrib import admin
from .models import Book , Review


class ReviewInline(admin.TabularInline):
        model = Review


class BookAdmin(admin.ModelAdmin):
    inines = [
        ReviewInline,
    ]

    list_display = ("title","author","publisher","genre","isbn","summary","location","availability")




admin.site.register(Book, BookAdmin)