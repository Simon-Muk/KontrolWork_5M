from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Post

        fields = [
            'id',
            'author',
            'title',
            'body',
            'is_published',
            'created_at',
            'updated_at'
        ]


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment

        fields = [
            'id',
            'author',
            'body',
            'is_approved',
            'created_at',
            'updated_at'
        ]