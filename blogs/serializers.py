from rest_framework import serializers
from .models import Blog, Comment

class SerializerComment(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'

class SerializerBlog(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'
    comments=SerializerComment(many=True, read_only=True)