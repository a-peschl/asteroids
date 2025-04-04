from circleshape import CircleShape
import pygame
from constants import *


class Shot(CircleShape):
    containers = None

    def __init__(self, x, y, velocity):
        super().__init__(x, y, 5)
        self.velocity = velocity
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius)
