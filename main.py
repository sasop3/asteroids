from sqlite3.dbapi2 import TimeFromTicks
import pygame
from constants import PLAYER_RADIUS, SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable) 
        
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field = AsteroidField()



    
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}" )

    while True:

        dt = clock.tick(60) / 1000 

        screen.fill("black")


        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        pygame.display.flip()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
        log_state()
                
    
    
if __name__ == "__main__":
    main()
