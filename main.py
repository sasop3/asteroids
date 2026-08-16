from sqlite3.dbapi2 import TimeFromTicks

import pygame
from constants import PLAYER_RADIUS, SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}" )

    while True:

        dt = clock.tick(60) / 1000 

        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
        log_state()
                
    
    
if __name__ == "__main__":
    main()
