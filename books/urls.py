from django.urls import path
from books import views

urlpatterns=[
    path('signup',views.SignUpView.as_view(),name='signup'),
    path('signin',views.LoginView.as_view(),name="signin"),
    path('home',views.IndexView.as_view(),name='index'),
    path('signout',views.SignOutView.as_view(),name='signout'),
    path('books',views.BookAddView.as_view(),name='add-book'),
    path('books/all',views.BookListView.as_view(),name='book-list'),
    path('books/details/<int:id>',views.BookDetailView.as_view(),name='book-detail')
]