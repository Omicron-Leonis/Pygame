import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My first game screen")

# Define colors
GREY = (58, 58, 58)

# Fill the background with grey
screen.fill(GREY)

# Load and scale the image
image_path = "your_image.png"  # Replace with the path to your image file
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (300, 300))

# Get the rectangle of the image and position it at the center
image_rect = image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# Blit the image onto the screen
screen.blit(image, image_rect)

# Update the display
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
