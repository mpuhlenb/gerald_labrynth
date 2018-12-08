# Gerald's Labrynth project for Simon learning pygame
import pygame
from screen import Screen

def main():
    running = True
    
    # Start screen
    screen = Screen()
    
    # Draw everything on the screen
    pygame.display.update()
    
    # main game loop run while running
    while running:
        # Check if Escape is pressed to end game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()                  

if __name__ == '__main__': main()