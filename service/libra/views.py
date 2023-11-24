from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


def book_list(request):
    books = Book.objects.all()
    return render(request, 'libra/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'libra/book_detail.html', {'book': book})


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
