from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Character, Connection

def _find_connection(x):
    return Character.objects.get(name=x)

@csrf_exempt
def character_index(request):
    # if request.method == "POST":
    #     # do the post stuff here
    #     pass
    # elif request.method == "GET":
    #     pass
    # elif request.method == "DELETE":
    #     pass
    # else:
    #     return HttpResponse(status=405)
    if request.method == "GET":
        character_list = Character.objects.all()
        output = json.dumps([c.as_JSON() for c in character_list])
        return HttpResponse(output)

    if request.method == "POST":
        body = json.loads(request.body)
        new_character = Character.objects.create(name=body["name"])
        new_allies = [Connection.objects.create(from_character=new_character, to_character=_find_connection(a), is_ally=True) for a in body["allies"]]
        new_enemies = [Connection.objects.create(from_character=new_character, to_character=_find_connection(e), is_enemy=True) for e in body["enemies"]]
        output = json.dumps(new_character.as_JSON())
        return HttpResponse(output)

    return HttpResponse(status=405)

@csrf_exempt
def single_character(request, character_id):
    # try:
    #     chosen_character = Character.objects.get(id=character_id)
    # except Character.DoesNotExist:
    #     return HttpResponse(status=404)
    if request.method == "GET":
        chosen_character = get_object_or_404(Character, id=character_id)
        output = json.dumps(chosen_character.as_JSON())
        return HttpResponse(output)

    if request.method == "PUT":
        chosen_character = get_object_or_404(Character, id=character_id)
        body = json.loads(request.body)

        chosen_character.name = body["name"]
        chosen_character.allies = body["allies"]
        chosen_character.enemies = body["enemies"]
        chosen_character.save()

        output = json.dumps(chosen_character.as_JSON())
        return HttpResponse(output)

    if request.method == "DELETE":
        chosen_character = get_object_or_404(Character, id=character_id)
        chosen_character.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=405)

def location_index(request):
    location_list = Location.objects.all()
    output = json.dumps([l.as_JSON() for l in location_list])
    return HttpResponse(output)
