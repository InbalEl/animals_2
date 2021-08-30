from django.urls import path
from .views import family, families, animal, animals

urlpatterns = [
    path('animal/<int:num>', animal, name='animal'),
    path('animals/', animals),
    path('family/<int:num>', family),
    path('families/', families),
]