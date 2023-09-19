from django.shortcuts import render
from django.http import HttpResponse
from django import forms;

tasks=[]

class NewTaskForm(forms.Form):
    task= forms.CharField(label="Add Task")
    priority= forms.IntegerField(label="Pritority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "front/index.html", {
        "tasks": tasks
    })
 
def login(request):
    return render(request, "front/login.html")

def register(request):
    return render(request, "front/register.html")

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "front/add.html", {
                "form": form
            })


    return render(request, "front/add.html", {
        "form": NewTaskForm()
    })