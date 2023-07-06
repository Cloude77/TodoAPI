from rest_framework import generics

from .models import ToDo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

