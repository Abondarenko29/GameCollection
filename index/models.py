from django.db import models


# Create your models here.
class GameType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    game_type = models.ManyToManyField(GameType, related_name="game_type")
    year = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.name
