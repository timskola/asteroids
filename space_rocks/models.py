# imports Vector2, used for handling positions and velocities in 2D space
from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import load_sprite

# vector pointing up, used for orientation
UP = Vector2(0, -1)

# makes a class called gameObject
class gameObject:
    def __init__(self, position, sprite, velocity):
        # Translates the position into Vector2 values for easier manipulation.
        self.position = Vector2(position)
        # Assigns the sprite to the object, will be used for drawing the object.
        self.sprite = sprite
        # Calculates the radius of the object based on the sprite's width.
        self.radius = sprite.get_width() / 2
        # Translates the velocity into Vector2 values for easier manipulation.
        self.velocity = Vector2(velocity)

    # Defines the draw function, which draws the object on the given surface.
    def draw(self, surface):
        # Calculates the position to blit the sprite so that it is centered on the object's position.
        blit_position = self.position - Vector2(self.radius)
        # Draws the sprite on the surface at the calculated position.
        surface.blit(self.sprite, blit_position)

    # Defines move function, updates position based on velocity.
    def move(self):
        self.position = self.position + self.velocity
        self.velocity *= self.FRICTION
    # Collision detection, checks if this object collides with another object.
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

class Spaceship(gameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    FRICTION = 0.98
    def __init__(self, position):
        # Make a copy of the original UP vector
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite("spaceship"), Vector2(0))
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
    
    
    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 0.25)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
        
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
    
    