from django.contrib import admin
from .models import Character, Connection, Location, House

admin.site.register(Character)
admin.site.register(Connection)
admin.site.register(Location)
admin.site.register(House)
