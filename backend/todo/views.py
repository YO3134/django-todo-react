from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    # Class 'Todo' has no 'objects' member
    # https://stackoverflow.com/questions/45135263/class-has-no-objects-member
