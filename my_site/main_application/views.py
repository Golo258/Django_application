from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


def index(response, list_id):  # getting argument / in web browser
    todoList = ToDoList.objects.get(id=list_id)
    item = todoList.item_set.get(id = 1)
    return HttpResponse("<h1>%s</h1></br><p>%s</p>" % (todoList.name, str(item.text)))
