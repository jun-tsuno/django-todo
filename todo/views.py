from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo
from .forms import TodoCreateForm

# Create your views here.

class TodoView(ListView):
  template_name = 'todo/todo-list.html'
  model = Todo
  ordering = ['-date']
  context_object_name = 'todos'

  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    for todo in context['todos']:
      todo.status_display = todo.get_status_display()
    return context


class TodoDetailView(DetailView):
  template_name = 'todo/todo-detail.html'
  model = Todo
  context_object_name = 'todo'

  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    context['todo'].status_display = context['todo'].get_status_display()
    return context


class TodoCreateView(View):
  def get(self, request):
    return render(request, 'todo/todo-create.html', {
      'form': TodoCreateForm()
    })

  def post(self, request):
    create_form =  TodoCreateForm(request.POST)

    if create_form.is_valid():
      create_form.save()
      return HttpResponseRedirect(reverse('top-page'))

    return render(request, 'todo/todo-create.html', {
      'form': create_form
    })

class TodoUpdateView(UpdateView):
  model = Todo
  template_name = 'todo/todo-detail.html'
  fields = ['status']
  success_url = '/'


class TodoDeleteView(DeleteView):
  model = Todo
  template_name = 'todo/todo-detail.html'
  success_url = '/'

# class TodoCreateView(CreateView):
#   template_name = 'todo/todo-create.html'
#   model = Todo
#   fields = ['text', 'status']
#   success_url = 'top-page'