from django.shortcuts import render, get_object_or_404
from .models import Animal, Family

def animal(req, num):
    animal = get_object_or_404(Animal, id=num)
    return render(req, 'info/animal.html', {'animal': animal})

def family(req, num):
    family = get_object_or_404(Family, id=num)
    return render(req, 'info/family.html', {'family': family})

def animals(req):
    animals = Animal.objects.all()
    return render(req, 'info/animals.html', {'animals': animals})

def families(req):
    families = Family.objects.all()
    return render(req, 'info/families.html', {'families': families})