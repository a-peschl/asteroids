from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        current_position = self.position
        velocity = self.velocity
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randome_angle = random.uniform(20, 50)
            vector_1 = velocity.rotate(randome_angle)
            vector_2 = velocity.rotate(-randome_angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(current_position.x, current_position.y, new_radius)
            asteroid_2 = Asteroid(current_position.x, current_position.y, new_radius)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2




