from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from circleshape import CircleShape
from constants import LINE_WIDTH as line_width
from shot import Shot
import pygame
class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class (CircleShape) constructor if it handles position
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0
    def draw(self, screen):
         pygame.draw.polygon(screen, "white", self.triangle(), line_width)
        # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        
    def shoot(self):
    # 1. Create the shot at the player's current position
     new_shot = Shot(self.position.x, self.position.y)
    
    # 2. Start with a forward-facing vector (0, 1)
    # Note: In Pygame, (0, 1) points down, but .rotate() 
    # will align it with your player's internal rotation logic.
     velocity = pygame.Vector2(0, 1)
    
    # 3. Rotate the vector to match the player's direction
     velocity = velocity.rotate(self.rotation)
    
    # 4. Scale by speed constants
     new_shot.velocity = velocity * PLAYER_SHOOT_SPEED