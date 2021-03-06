import uuid
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=10)
    isbn = models.IntegerField()
    summary = models.CharField(max_length=10000, default= 'summary')
    location = models.CharField(max_length=1000)
    availability = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True)

class Meta:
    indexes = [
        models.Index(fields=['id'], name='id_index')
    ]
    permissions = [
        ('special_status' , 'Can read all books')
    ]


    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs=[str(self.id)])



class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',

    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.review





