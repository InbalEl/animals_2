from django.shortcuts import render, get_object_or_404
from .models import Animal, Family

def animal(req, num):
    animal = get_object_or_404(Animal, id=num)
    return render(req, 'info/animal.html', {'animal': animal, 'family': animal.family})

def family(req, num):
    family = get_object_or_404(Family, id=num)
    animals = family.animal_set.all().order_by('name')
    return render(req, 'info/family.html', {'family': family, 'animals': animals, 'size': len(animals)})

def animals(req):
    animals = Animal.objects.all().order_by('family__name')
    return render(req, 'info/animals.html', {'animals': animals})

def animals_speed(req):
    animals = Animal.objects.all().order_by('Speed')
    return render(req, 'info/animals_speed.html', {'animals': animals})

def families(req):
    families = Family.objects.all()
    return render(req, 'info/families.html', {'families': families})