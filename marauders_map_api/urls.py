from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.character_index),
    path('characters/<int:character_id>', views.single_character),
    path('locations/', views.location_index),
]
