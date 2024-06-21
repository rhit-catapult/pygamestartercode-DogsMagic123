import pygame
import sys
import random


# TODO: Create a Ball class.
class Ball():


 def __init__(self, screen, x, y ):
     self.radius = random.randint(1, 40)
     self.speed_x = random.randint(1, 15)
     self.speed_y = random.randint(1,15)
     self.color_red = random.randint(0, 250)
     self.color_green = random.randint(0, 255)
     self.color_blue = random.randint(0, 255)


 def draw(self):
     pygame.draw.circle(self.screen, pygame.Color(self.color_red, self.color_green, self.color_blue), (self.x,self.y), (self.radius))


 def move(self):
     self.y += self.speed_y
     self.x += self.speed_x
     if self.y < 0:
         self.speed_y *= -1
     if self.y > self.screen.get_height():
         self.speed_y *= -1
     if self.x < 0:
         self.speed_x *= -1
     self.y = y
     self.x = x
     self.screen = screen
     if self.x > self.screen.get_width():
         self.speed_x *= -1


# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y

# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()



    # TODO: Create an instance of the Ball class called ball1
    test_ball = Ball(screen, 400, 400)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        test_ball.draw()
        test_ball.move()

        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
