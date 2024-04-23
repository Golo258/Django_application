from django.db import models


# database Models
class ToDoList(models.Model):
    name = models.CharField(max_length=200)  # attribute = class variable

    def __str__(self):
        return self.name


class Item(models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)  # creating to do list in item
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
