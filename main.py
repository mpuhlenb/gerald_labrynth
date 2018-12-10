# Gerald's Labrynth project for Simon learning pygame
import pygame
from screen import Screen
from gerald import Gerald

def main():
    running = True
    
    # Start screen
    screen = Screen()
    
    # Create Gerald
    gerald = Gerald()
    
    render_gerald = pygame.sprite.RenderUpdates()
    render_gerald.add(gerald)
    render_gerald.draw(screen.surface)
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