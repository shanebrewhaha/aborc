import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adventure Game")

# Font
font = pygame.font.Font(None, 36)

# Function to draw text on the screen
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

# Function to handle the first choice
def first_choice():
    screen.fill(BLACK)
    draw_text("You see three paths in front of you.", 20, 20)
    draw_text("1. Take the path to the left.", 20, 60)
    draw_text("2. Take the path straight ahead.", 20, 100)
    draw_text("3. Take the path to the right.", 20, 140)
    pygame.display.flip()

    choice = get_choice(3)
    if choice == 1:
        left_path()
    elif choice == 2:
        straight_path()
    elif choice == 3:
        right_path()

# Function for the left path
def left_path():
    screen.fill(BLACK)
    draw_text("You take the path to the left and encounter a wild bear!", 20, 20)
    draw_text("1. Try to fight the bear.", 20, 60)
    draw_text("2. Run away.", 20, 100)
    pygame.display.flip()

    choice = get_choice(2)
    if choice == 1:
        game_over("You bravely fight the bear but unfortunately, it is too strong. You did not survive.")
    elif choice == 2:
        game_over("You run away and manage to escape the bear, but you are lost in the forest.")

# Function for the straight path
def straight_path():
    screen.fill(BLACK)
    draw_text("You take the path straight ahead and find a treasure chest!", 20, 20)
    draw_text("1. Open the chest.", 20, 60)
    draw_text("2. Leave the chest and continue walking.", 20, 100)
    pygame.display.flip()

    choice = get_choice(2)
    if choice == 1:
        game_over("You open the chest and find a pile of gold! You are rich!")
    elif choice == 2:
        game_over("You leave the chest and continue walking. Eventually, you find your way out of the forest.")

# Function for the right path
def right_path():
    screen.fill(BLACK)
    draw_text("You take the path to the right and encounter a wise old man.", 20, 20)
    draw_text("He offers you a choice between wisdom and wealth.", 20, 60)
    draw_text("1. Choose wisdom.", 20, 100)
    draw_text("2. Choose wealth.", 20, 140)
    pygame.display.flip()

    choice = get_choice(2)
    if choice == 1:
        game_over("The old man grants you immense wisdom. You live a long and fulfilling life.")
    elif choice == 2:
        game_over("The old man gives you a bag of gold, but you soon realize it brings more trouble than joy.")

# Function to end the game
def game_over(message):
    screen.fill(BLACK)
    draw_text(message, 20, 20)
    draw_text("Game Over. Press any key to exit.", 20, 60)
    pygame.display.flip()
    wait_for_key()
    sys.exit()

# Function to wait for the player to press a key
def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

# Function to get the player's choice
def get_choice(max_choice):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and max_choice >= 1:
                    return 1
                if event.key == pygame.K_2 and max_choice >= 2:
                    return 2
                if event.key == pygame.K_3 and max_choice >= 3:
                    return 3

# Main function to start the game
def main():
    screen.fill(BLACK)
    draw_text("Welcome to the Adventure Game!", 20, 20)
    draw_text("Press any key to start.", 20, 60)
    pygame.display.flip()
    wait_for_key()
    first_choice()

# Run the game
if __name__ == "__main__":
    main()
