from django.shortcuts import render
from rest_framework import viewsets  # add this
from .serializers import TodoSerializer  # add this
from .models import Todo  # add this


class TodoView(viewsets.ModelViewSet):  # add this
    serializer_class = TodoSerializer  # add this
    queryset = Todo.objects.all()  # add this
    # Class 'Todo' has no 'objects' member
    # https://stackoverflow.com/questions/45135263/class-has-no-objects-member
