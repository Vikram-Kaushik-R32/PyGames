import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Simple Pygame Application")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Ball settings
ball_pos = [100, 100]
ball_radius = 20
ball_speed = [2, 2]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce the ball off the edges
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > screen_size[0]:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > screen_size[1]:
        ball_speed[1] = -ball_speed[1]

    # Fill the screen with white
    screen.fill(white)

    # Draw the ball
    pygame.draw.circle(screen, blue, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)
