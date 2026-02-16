from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>ICT12367 SPU</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1>")

def form(request):
    return render(request, 'form.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ ตามด้วยข้อมูลนักศึกษา เช่น รหัสนักศึกษา ชื่อ นามสกุล</h1>")