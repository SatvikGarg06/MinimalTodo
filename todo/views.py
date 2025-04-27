from django.shortcuts import render, get_object_or_404

from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from .models import ToDoItem
from .forms import TaskForm, EditTaskForm

from datetime import date

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm
    return render(request, 'registration/register.html', context={'form': form})

@login_required
def all_todos(request):
    return render(request, "todos.html", context={'todos': ToDoItem.objects.filter(owner = request.user)})

def home(request):
    return render(request, "home.html")

@login_required
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.task_name = form.cleaned_data['task_name']
            new_task.task_desc = form.cleaned_data['task_desc']
            new_task.due_date = form.cleaned_data['due_date']
            new_task.date_added = date.today()
            new_task.owner = request.user
            new_task.save()
            return HttpResponseRedirect(reverse('todos'))
    else:
        form = TaskForm()
    return render(request, "new_task.html", {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(ToDoItem, pk = pk)
    task.delete()
    return HttpResponseRedirect(reverse('todos'))

@login_required
def edit_task(request, pk):
    task = get_object_or_404(ToDoItem, pk = pk)
    print(task)
    if request.method == 'POST':
        form = EditTaskForm(request.POST)
        form.is_valid()
        task.task_name = form.cleaned_data['task_name']
        task.task_desc = form.cleaned_data['task_desc']
        task.due_date = form.cleaned_data['due_date']
        task.save()
        return HttpResponseRedirect(reverse('todos'))
    else:
        form = EditTaskForm(initial={'task_name': task.task_name, 'task_desc': task.task_desc, 'due_date': task.due_date})
    
    context = {
        'form': form,
        'task': task,
        'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else None
    }
    return render(request, 'edit_task.html', context = context)