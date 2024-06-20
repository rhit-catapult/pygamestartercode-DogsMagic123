import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # TODO 1: Create an image with the 2dogs.JPG image
    image1 = pygame.image.load("2dogs.JPG")
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    image1 = pygame.transform.scale(image1,(IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    myfont = pygame.font.SysFont("arial", 28)
    myfont2 = pygame.font.SysFont("comicsans", 32)

    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = myfont.render("toe dogs", True, pygame.Color("pink"))
    caption2 = myfont2.render("I love theses toe dogs", True, pygame.Color("black"))

    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark = pygame.mixer.Sound("bark.mp3")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONUP:
                bark.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image1,(0, 0))

        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption1, (50,400))
        screen.blit(caption2, (screen.get_width()/6 ,screen.get_width()/2+220))
        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()

'''
images
before the loop ---> image1 = pygame.image.load
later -----> screen.blit(image1, (0,0))

text
create text ----> my_font = pygame.font.SysFont("arial", 28)
caption1 = my_font.render("toe dogs", True, pygame.Color("pink"))
create caption -----> 
show caption on screen ----->  screen.blit(caption1, (50,400))
'''

