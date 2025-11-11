# importerar load funktionen från pygame.image modulen
from pygame.image import load

# Definierar en funktion som laddar in en sprite från assets mappen
def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

# kollar ifall "with_alpha" är sant, vilket gör bilden genomskinlig.
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()