from django.urls import path
from . import views

urlpatterns = [
    path("<int:list_id>", views.index, name="index"),  # home directory /
    path("", views.home, name="home"),  # home directory /
    path("create/", views.create, name="create")  # home directory /

]

