from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


app_name = "rooms"

urlpatterns = [
    path("", views.RoomsView.as_view()),
    path("<int:pk>", views.RoomView.as_view()),
]
