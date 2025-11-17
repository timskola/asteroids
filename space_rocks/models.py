# imports Vector2, used for handling positions and velocities in 2D space
from pygame.math import Vector2

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
    # Collision detection, checks if this object collides with another object.
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius