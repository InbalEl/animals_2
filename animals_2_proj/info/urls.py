from django.urls import path
from .views import family, families, animal, animals, animals_speed

urlpatterns = [
    path('animal/<int:num>', animal, name='animal'),
    path('animals/', animals, name='animals'),
    path('animals/speed/', animals_speed, name='animals_speed'),
    path('family/<int:num>', family, name='family'),
    path('families/', families, name='families'),
]