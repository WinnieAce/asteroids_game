from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        random_angle =random.uniform(20, 50)
        
        a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        
        a.velocity = self.velocity.rotate(random_angle) * 1.2
        b.velocity = self.velocity.rotate(-random_angle) * 1.2
        
        
    