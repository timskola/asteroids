import pygame

from models import gameObject
from utils import load_sprite

# Definerar huvudklassen för spelet, kallad "Asteroids" eftersom det är en kopia av atari asteroids.
class Asteroids:
    # Definierar init funktionen, pygame initieras och gör att skärmen är rätt upplösning.
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space_background", False)
        self.clock = pygame.time.Clock()
        self.spaceship = gameObject(
            (400, 300), load_sprite("spaceship"), (0, 0)
        )
        self.asteroid = gameObject(
            (400, 300), load_sprite("evilmeteorite"), (1, 0)
        )
    # Definierar main_loop detta är loopen som gör att skärmen uppdateras, spelet faktiskt körs och att den känner av inputs.
    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()
    
    # Initialiserar pygame och gör att den dära saken i hörnet av programmet visar rätt namn.        
    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Asteroids but awesome")

    # hanterar input, inte klar
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
               event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    # processar spel logiken, inte klar
    def _process_game_logic(self):
        self.spaceship.move()
        self.asteroid.move()

    # Definierar draw funktionen, den ritar allt på skärmen.
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)