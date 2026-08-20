from random import random, uniform
from typing import override
import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,color="white",center=self.position,radius=self.radius,width=LINE_WIDTH)


    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(ASTEROID_MIN_RADIUS >= self.radius):
            return
        else:
            log_event("asteroid_split")
            old_radius = self.radius
            angle = uniform(20,50)
            first_new_angle = self.velocity.rotate(angle)
            second_new_angle = self.velocity.rotate(-angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            first_asteroid = Asteroid(radius=new_radius,x=self.position.x,y=self.position.y)
            first_asteroid.velocity = first_new_angle * 1.2
            
            second_asteroid = Asteroid(radius=new_radius,x=self.position.x,y=self.position.y)
            second_asteroid.velocity = second_new_angle * 1.2
