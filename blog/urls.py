from django.urls import path

from .views import *


urlpatterns = [

    path(
        'posts/',
        PostListCreateView.as_view()
    ),

    path(
        'posts/<int:pk>/',
        PostDetailView.as_view()
    ),

    path(
        'posts/<int:pk>/comments/',
        CommentListView.as_view()
    ),

    path(
        'posts/<int:pk>/comments/create/',
        CommentCreateView.as_view()
    ),
]
