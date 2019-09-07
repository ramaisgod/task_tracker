from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def home_page(request):
    context = {
        'obj_project': Project.objects.all(),
        'obj_task': Task.objects.all(),
        'obj_activity': Activity.objects.all(),
    }
    return render(request, 'home.html', context)

def add_project(request):
    context = {
        'form': ProjectForm(),
    }
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            context['message'] = "Data has been saved !!!"
            return render(request, 'add_project.html', context)
        else:
            context['form'] = form
            context['message'] = "Please enter valid data."
            return render(request, 'add_project.html', context)            
    return render(request, 'add_project.html', context)

def project_list(request):
    context = {
        'obj_project': Project.objects.all(),
    }           
    return render(request, 'project_list.html', context)

def add_task(request):
    context = {
        'form': TaskForm(),
    }
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            context['message'] = "Data has been saved !!!"
            return render(request, 'add_task.html', context)
        else:
            context['form'] = form
            context['message'] = "Please enter valid data."
            return render(request, 'add_task.html', context)            
    return render(request, 'add_task.html', context)

def add_activity(request):
    context = {
        'form': ActivityForm(),
    }
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            context['message'] = "Data has been saved !!!"
            return render(request, 'add_activity.html', context)
        else:
            print(form.errors)
            context['form'] = form
            context['message'] = "Please enter valid data."
            return render(request, 'add_activity.html', context)            
    return render(request, 'add_activity.html', context)

