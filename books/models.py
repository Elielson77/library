from django.db import models
from uuid import uuid4


def upload_image_book(instance, file_name):
    return f"{instance.id_book}-{file_name}"


# Create your models here.
class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to=upload_image_book, blank=True, null=True)
