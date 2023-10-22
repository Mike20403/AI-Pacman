import pygame
import sys
from pygame.locals import *
import levels.level1 as level1
import levels.level2 as level2
import levels.level3 as level3
# Initialize pygame
pygame.init()

# Create the display surface
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Pac-Man Menu")

# Set up colors and fonts
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
FONT = pygame.font.Font(None, 36)

# Menu options
options = ["Level 1: No Monsters", "Level 2: Stationary Monster","Level 3: Pac-Man's blind"]

# Position for menu items
menu_rects = [FONT.render("   " + option, True, WHITE).get_rect(center=(200, 100 + index * 50)) for index, option in enumerate(options)]

# Game loop
selected_option = 0
running = True

def draw_menu():
    screen.fill((0, 0, 0))
    for index, rect in enumerate(menu_rects):
        color = YELLOW if index == selected_option else WHITE
        text = FONT.render("-> " + options[index] if index == selected_option else "   " + options[index], True, color)
        screen.blit(text, rect)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            for index, rect in enumerate(menu_rects):
                if rect.collidepoint(event.pos):
                    selected_option = index

        if event.type == KEYDOWN:
            if event.key == K_UP:
                selected_option = (selected_option - 1) % len(options)
            elif event.key == K_DOWN:
                selected_option = (selected_option + 1) % len(options)
            elif event.key == K_RETURN:
                if selected_option == 0:
                    level1.main()  # Start Level 1
                elif selected_option == 1:
                    level2.main()  # Start Level 2
                elif selected_option == 2:
                    level3.main()

    draw_menu()
    pygame.display.flip()

# Clean up and quit pygame after the game loop exits
pygame.quit()
sys.exit()
