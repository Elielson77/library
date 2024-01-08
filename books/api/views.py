from rest_framework import viewsets
from books.api.serializers import BooksSerializers
from books.models import Books


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializers
    queryset = Books.objects.all()
