from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from models import TodoList,TodoItem
class TodoListView(ListView):
    model=TodoList


class TodoCreateView(CreateView):
    model = TodoList
    fields = ['name','date']
    def get_success_url(self):
        return reverse("display-lists")

class TodoUpdateView(UpdateView):
    model = TodoList
    fields = ['name','date']

    def get_object(self, queryset=None):
        return TodoList.objects.get(pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse("display-lists")
class TodoDeleteView(DeleteView):
    model = TodoList
    success_url = reverse_lazy('delete-data')
    def get_object(self, queryset=None):
        return TodoList.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse("display-lists")

class TodoDetailsView(DetailView):
    model = TodoList
    def get_object(self, queryset=None):
        return TodoList.objects.get(pk=self.kwargs.get("id"))

class TodoItemCreateView(CreateView):
    model = TodoItem
    fields = ['item_id','description','duedate','status']

    def get_success_url(self):
        id = self.request.POST.get('item_id')
        return reverse("display-items",args=(id,))

class TodoItemUpdateView(UpdateView):
    model = TodoItem
    fields = ['item_id', 'description', 'duedate', 'status']
    def get_object(self, queryset=None):
        return TodoItem.objects.get(pk=self.kwargs.get("pk"))

    def get_success_url(self):
        id = self.request.POST.get('item_id')
        return reverse("display-items", args=(id,))

class TodoItemDeleteView(DeleteView):
    model = TodoItem
    def get_object(self, queryset=None):
        return TodoItem.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        id=self.request.POST.get('deleteitem')
        return reverse("display-items", args=(id,))

class TodoItemDetailsView(DetailView):
    model = TodoItem
    def get_object(self, queryset=None):
        return TodoItem.objects.get(pk=self.kwargs.get("id"))