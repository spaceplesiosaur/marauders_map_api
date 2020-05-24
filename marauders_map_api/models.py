from django.db import models

BIG_STRING = 60000

class Character(models.Model):
    name = models.CharField(max_length=BIG_STRING)
    connections = models.ManyToManyField("self", through="Connection")
    image = models.ImageField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def as_JSON(self):
        return {
            'name': self.name,
            'id': self.id,
            #'connections': [character.name for character in self.connections.all()],
            'allies': [
                        connection.to_character.name
                            for connection
                            in Connection.objects.filter(from_character=self, is_ally=True)
                            ],
            'enemies': [
                        connection.to_character.name
                            for connection
                            in Connection.objects.filter(from_character=self, is_enemy=True)
                            ],
            'image': self.image.url
        }


class Connection(models.Model):
    from_character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="outgoing_connections")
    to_character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="incoming_connections")
    is_ally = models.BooleanField(default=True)
    is_enemy = models.BooleanField(default=False)


class Location(models.Model):
    name = models.CharField(max_length=BIG_STRING, unique=True)
    current_occupants = models.ManyToManyField(Character)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def as_JSON(self):
        return {
            'name': self.name,
            'current_occupants': self.current_occupants.all()
        }

class House(models.Model):
    name = models.CharField(max_length=BIG_STRING)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    head = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="head")
    members = models.ManyToManyField(Character, related_name="house")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
