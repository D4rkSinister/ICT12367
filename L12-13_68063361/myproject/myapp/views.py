from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from myapp.models import Person

# Create your views here.
def index(request):
    # 1. ดึงข้อมูลประชากรทั้งหมดจากฐานข้อมูล (กรณีที่ยังไม่ได้ค้นหา)
    all_persons = Person.objects.all()
    
    # 2. รับค่าคำค้นหาจากผู้ใช้ (name="q")
    query = request.GET.get('q')
    
    # 3. ตรวจสอบว่ามีคำค้นหาลุกพิมพ์สงมหรือไม่
    if query:
        # ถ้ามีคำค้นหา ให้นำ all_persons มากรองข้อมูลเลขพจจากคำค้นหา
        all_persons = all_persons.filter(Q(name__icontains=query) | Q(age__icontains=query))
    
    # 4. ส่งข้อมูลไปแสดงผลที่ template (ค่าไม่มี query ก็จะแสดงทั้งหมดควรตัน 1)
    return render(request,"index.html",{"all_persons": all_persons, "query": query})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        person = Person.objects.create(
            name=name,
            age=age
        )
        return redirect("/")
    else:
        return render(request,"form.html")

def edit(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect("/")
    else:
        return render(request, "form.html", {"person": person})

def delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect("/")