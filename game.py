import pygame

# Definerar huvudklassen för spelet, kallad "Asteroids" eftersom det är en kopia av atari asteroids.
class Asteroids:
    # Definierar init funktionen, pygame initieras och gör att skärmen är rätt upplösning.
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((1200, 900))

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
        pass

    # Definierar draw funktionen, den ritar allt på skärmen.
    def _draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()