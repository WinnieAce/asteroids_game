import pygame 
from constants import *

def main():
    # set screen discplay
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # refresh screen
	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
       			return

		screen.fill((0, 90, 0))
		pygame.display.flip()


	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()

