from http import HTTPStatus
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book, Author
from .serializers import BookSerializer

class BooksAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data, status=HTTPStatus.OK)

    def post(self, request):
        books_serializer = BookSerializer(data=request.data)
        if books_serializer.is_valid():
            books_serializer.save()
            return Response(books_serializer.data, status=HTTPStatus.CREATED)
        return Response(books_serializer.errors, status=HTTPStatus.BAD_REQUEST)