from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_persons = Person.objects.all()
    return render(request,"index.html",{"all_persons": all_persons})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")