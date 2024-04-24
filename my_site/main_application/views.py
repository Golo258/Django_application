from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, list_id):  # getting argument / in web browser
    todoList = ToDoList.objects.get(id=list_id)
    if response.method == "POST":
        print(f"response = {response.POST }\n")
        if response.POST.get('save'):
            for item in todoList.item_set.all():
                if response.POST.get('c' + str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get('newItem'):
            content = response.POST.get("new_item_added")
            print(f"{content =}")
            if len(content) > 2:
                todoList.item_set.create(text= content, complete=False)
            else:
                print("Invalid input")

    return render(response,
                  'main_application/list.html',
                  {"list": todoList})


def home(response):
    return render(response,
                  'main_application/home.html',
                  {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            data = form.cleaned_data["name"]
            new_list = ToDoList(name=data)
            new_list.save()

        return HttpResponseRedirect("/%i" %new_list.id)

    else:
        form = CreateNewList()

    return render(response,
                      'main_application/create.html',
                      {"form": form})


'''
   item = todoList.item_set.get(id = 1)
    return HttpResponse("<h1>%s</h1></br><p>%s</p>" % (todoList.name, str(item.text)))

'''
