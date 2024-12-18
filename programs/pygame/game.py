import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Basket properties
basket_width = 100
basket_height = 20
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - basket_height - 20
basket_speed = 10

# Falling object properties
object_width = 30
object_height = 30
falling_objects = []
falling_speed = 5

# Score and font
score = 0
font = pygame.font.Font(None, 36)

# Game over flag
game_over = False

# Function to create falling objects
def create_falling_object():
    obj_type = random.choice(["apple", "bomb"])
    x = random.randint(0, WIDTH - object_width)
    y = -object_height
    color = GREEN if obj_type == "apple" else RED
    falling_objects.append({"x": x, "y": y, "type": obj_type, "color": color})

# Function to display the score
def display_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Create a new falling object occasionally
    if random.randint(1, 30) == 1:
        create_falling_object()

    # Update falling objects
    for obj in falling_objects[:]:
        obj["y"] += falling_speed
        pygame.draw.rect(screen, obj["color"], (obj["x"], obj["y"], object_width, object_height))

        # Check for catching or missing the objects
        if obj["y"] > HEIGHT:
            falling_objects.remove(obj)
        elif (basket_x < obj["x"] < basket_x + basket_width) and (basket_y < obj["y"] < basket_y + basket_height):
            if obj["type"] == "apple":
                score += 1
                falling_objects.remove(obj)
            elif obj["type"] == "bomb":
                game_over = True

    # Draw the basket
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))

    # Display score
    display_score()

    # Check for game over
    if game_over:
        screen.fill(RED)
        game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_restart = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # Reset game state
                    falling_objects.clear()
                    score = 0
                    game_over = False
                    basket_x = (WIDTH - basket_width) // 2
                    waiting_for_restart = False

    # Refresh the screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
