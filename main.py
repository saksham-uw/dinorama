# -----------------  Libraries  ----------------- #


import pygame
import os
import random
import sys


# -----------------  Initialize pygame  ----------------- #


pygame.init()


# -----------------  Global Constants  ----------------- #


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("assets/dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("assets/dino", "DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join("assets/dino", "DinoJump.png"))

GROUND = pygame.image.load(os.path.join("assets/other", "Track.png"))

FONT = pygame.font.Font('freesansbold.ttf', 20)


# -----------------  Dino Class  ----------------- #


class Dino:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self, img=RUNNING[0]):
        self.imgage = img
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS,
                                img.get_width(), img.get_height())
        self.step_index = 0

    def update(self):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.imgage = JUMPING
        if self.dino_jump:
            self.rect.y -= (self.jump_vel * 4)
            self.jump_vel -= 0.8
        if self.jump_vel <= -(self.JUMP_VEL):
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    def run(self):
        self.imgage = RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.imgage, (self.rect.x, self.rect.y))


# -----------------  main() function  ----------------- #


def main():
    clock = pygame.time.Clock()

    # Ability to display multiple dinos for AI implementation
    dinos = [Dino()]

    run = True
    while(run):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        SCREEN.fill((255, 255, 255))

        for dino in dinos:
            dino.update()
            dino.draw(SCREEN)

        user_input = pygame.key.get_pressed()

        for (i, dino) in enumerate(dinos):
            if user_input[pygame.K_SPACE]:
                dino.dino_jump = True
                dino.dino_run = False

        clock.tick(30)
        pygame.display.update()


# -----------------  Driver Code  ----------------- #


main()


# -----------------  xxxxxxxxx  ----------------- #
