from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from .models import Post, Comment
from .serialazers import (
    PostSerializer,
    CommentSerializer
)
from .permissions import IsOwner


class PostListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = PostSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        return Post.objects.filter(
            is_published=True
        )

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            author=self.request.user
        )

class PostDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = PostSerializer

    queryset = Post.objects.all()

    permission_classes = [IsOwner]


class IsOwnerOrReadOnly(
    BasePermission
):
    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
    


class CommentListView(
    generics.ListAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs['pk']
        )
    

class CommentCreateView(
    generics.CreateAPIView
):
    serializer_class = CommentSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            author=self.request.user,
            post_id=self.kwargs['pk']
        )