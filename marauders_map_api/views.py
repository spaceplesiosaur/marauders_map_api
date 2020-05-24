from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Character

def character_index(request):
    character_list = Character.objects.all()
    output = json.dumps([c.as_JSON() for c in character_list])
    return HttpResponse(output)

def single_character(request, character_id):
    chosen_character = Character.objects.filter(id=character_id)[0]
    #revisit
    output = json.dumps(chosen_character.as_JSON())
    return HttpResponse(output)

def location_index(request):
    location_list = Location.objects.all()
    output = json.dumps([l.as_JSON() for l in location_list])
    return HttpResponse(output)
