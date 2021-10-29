from django.urls import path
from alpha import views

urlpatterns = [path("user", views.handle_request, name="user")]
