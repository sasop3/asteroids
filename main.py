import pygame
import sys
from sqlite3.dbapi2 import TimeFromTicks
from constants import PLAYER_RADIUS, SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot 

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable) 
    Shot.containers = (shots,drawable,updatable)
        
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
        for a in asteroids:
            if(a.collides_with(player)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if(a.collides_with(s)):
                    log_event("asteroid_shot")
                    s.kill()
                    a.kill()    

        pygame.display.flip()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
        log_state()
                
    
    
if __name__ == "__main__":
    main()
