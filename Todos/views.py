from django.shortcuts import *

# Create your views here.
from Todos.models import *
from django.contrib import admin
admin.autodiscover()

def text(request,id):
    items = TodoItem.objects.filter(item_id_id=id)
    templete = loader.get_template("items.html")
    result = templete.render(context={"items": items})
    return HttpResponse(result)

def lists(request):
    todos = TodoList.objects.all()
    templete = loader.get_template("text.html")
    result = templete.render(context={"todos": todos})
    return HttpResponse(result)

