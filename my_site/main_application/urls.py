from django.urls import path
from . import views

urlpatterns = [
    path("<int:list_id>", views.index, name="index"),  # home directory /
]

