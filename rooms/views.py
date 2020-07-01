from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer, BigRoomSerializer

# Customize pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class ListRoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = LargeResultsSetPagination


class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer
