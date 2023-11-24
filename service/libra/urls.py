from django.urls import path
from .views import book_list, book_detail, BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('book_detail/', book_detail, name='book_detail'),
    path('book_detail/<int:book_id>/', book_detail, name='book_detail'),
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

]
