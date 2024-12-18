import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Running Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Load car image and resize it
car_img = pygame.Surface((50, 100))
car_img.fill(BLUE)

# Car attributes
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Obstacle attributes
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 7
obstacle_color = RED

# List to store obstacles
obstacles = []

# Function to create obstacles
def create_obstacle():
    obstacle_x = random.randint(0, WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

# Function to draw obstacles
def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle)

# Function to move obstacles
def move_obstacles():
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)

# Function to check for collisions
def check_collision(car_rect):
    for obstacle in obstacles:
        if car_rect.colliderect(obstacle):
            return True
    return False

# Main game loop
def game_loop():
    global car_x
    running = True
    score = 0

    # Create initial obstacles
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                create_obstacle()

        # Handle car movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
            car_x += car_speed

        # Car rectangle for collision detection
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        screen.blit(car_img, (car_x, car_y))

        # Move and draw obstacles
        move_obstacles()
        draw_obstacles()

        # Check for collision
        if check_collision(car_rect):
            font = pygame.font.SysFont(None, 55)
            text = font.render("Game Over!", True, RED)
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        # Update score
        score += 1
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Refresh the screen
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Run the game
game_loop()
