import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
CATCHER_WIDTH, CATCHER_HEIGHT = 80, 20
OBJECT_WIDTH, OBJECT_HEIGHT = 30, 30
FPS = 30
SPEED = 5
FALL_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Object class
class FallingObject:
    def __init__(self):
        self.reset()

    def fall(self):
        self.rect.y += FALL_SPEED

    def reset(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - OBJECT_WIDTH), 0, OBJECT_WIDTH, OBJECT_HEIGHT)

# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Catch the Falling Objects")
    clock = pygame.time.Clock()

    catcher = pygame.Rect(WIDTH // 2 - CATCHER_WIDTH // 2, HEIGHT - CATCHER_HEIGHT - 10, CATCHER_WIDTH, CATCHER_HEIGHT)
    falling_object = FallingObject()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and catcher.x > 0:
            catcher.x -= SPEED
        if keys[pygame.K_RIGHT] and catcher.x < WIDTH - CATCHER_WIDTH:
            catcher.x += SPEED

        falling_object.fall()

        # Check if the object is caught
        if falling_object.rect.colliderect(catcher):
            score += 1
            falling_object.reset()

        # Reset object if it falls past the screen
        if falling_object.rect.y > HEIGHT:
            # Restart game if object is missed
            print("Missed! Restarting...")
            score = 0  # Reset score
            falling_object.reset()  # Reset the falling object position

        # Drawing
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, catcher)
        pygame.draw.rect(screen, RED, falling_object.rect)

        # Display score
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(text, (10, 10))

        # Check for exit key
        if keys[pygame.K_q]:  # Press 'Q' to quit
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

