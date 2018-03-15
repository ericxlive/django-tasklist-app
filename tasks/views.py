from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):

    form = TaskForm()
    tasks = Task.objects.order_by('id')
    context = { 'tasks': tasks, 'form': form, }
    return render(request, 'index.html', context)

@require_POST
def add(request):

    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = Task(content=request.POST['content'])
        new_task.save()
    return redirect('index')

def complete(request, task_id):

    task = Task.objects.get(id=task_id)
    task.complete = True
    task.save()
    return redirect('index')

def delete_completed(request):

    Task.objects.filter(complete__exact = True).delete()
    return redirect('index')

def delete_all(request):

    Task.objects.all().delete()
    return redirect('index')