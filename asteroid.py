import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH as line_width
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)
    def update(self, dt):
        # must override
        self.position += self.velocity * dt
    