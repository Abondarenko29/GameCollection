import django_to_main
from index.models import Game, GameType


# default = GameType(name="default").save()
default = GameType.objects.get(id=1)
# Game.objects.create(
#     name="game1",
#     year=2025,
#     rating=9.7
# )
game = Game.objects.get(id=1)
# game.game_type.add(default)
