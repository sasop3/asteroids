import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill("black")
    pygame.display.flip()
    
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}" )

    while True:
        log_state()
        for event in pygame.event.get():
            if(event == pygame.QUIT):
                return
    
    
if __name__ == "__main__":
    main()
