from django.shortcuts import render
from .models import Item
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ItemSerializer
# Create your views here.


# class ListItemAPIView(ListAPIView):
#     """This Endpoint Returns all the available ToDo Items from the Database.[GET]"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


# class CreateItemAPIView(CreateAPIView):
#     """This Endpoint Create ToDo Items.[POST]"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


# class DeleteItemAPIView(DestroyAPIView):
#     """This Endpoint Delete a Specific Todo Item from the database.[DELETE]"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

class ItemAPIView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
