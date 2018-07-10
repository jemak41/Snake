import pygame
from pygame.locals import *
from sys import exit
import random
import os

pygame.init()
screen = pygame.display.set_mode((640,480), 0 , 32)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()



myfont = pygame.font.SysFont("comicsansms", 30)

class Snake(object):

    def __init__(self):
        self.cnt = 0
        self.snake = pygame.Rect(random.randint(1, 640), random.randint(1, 480), 10, 10)
        self.snake_head = pygame.Rect(random.randint(1, 640), random.randint(1, 480), 10, 10)
        self.foods = pygame.Rect(random.randint(1, 640), random.randint(1, 480), 5, 5)

        self.snake_width = 10
        self.snake_height = 10
        self.snakex = [299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299]
        self.snakey = [299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299,299]
        self.snakelen = len(self.snakex) - 1
        self.dirs = 0

    def eat(self):
        if self.snake.collidepoint(self.foods.left,self.foods.top):
            self.cnt += 1
            self.foods.left = random.randint(20, 620)
            self.foods.top = random.randint(20, 460)
            self.snakex.append(200)
            self.snakey.append(200)

    def wall(self):
        if self.snakey[self.snakelen] > 470 or self.snakey[self.snakelen] < 0 or self.snakex[self.snakelen] < 0 or self.snakex[self.snakelen] > 630:
            self.game_over()

    def collide_self(self):
        self.snakelen = len(self.snakex) - 1
        while self.snakelen >= 6:
            z = self.snakelen
            if pygame.Rect(self.snakex[0],self.snakey[0], 10, 10).colliderect(self.snakex[z], self.snakey[z], 10, 10):
                '''(self.snakex[0] + 10 > self.snakex[self.snakelen]) and (10 < self.snakex[self.snakelen] + 10) and (self.snakey[0] + 10 > self.snakey[self.snakelen]) and (
                self.snakey[0] < self.snakey[self.snakelen] + 10):'''
                self.game_over1()
            z -= 1

    def game_over(self):
        over = myfont.render("GAME OVER", 1,(255,0,0))
        screen.blit(over, (55, 55))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            pygame.display.update()
            clock.tick(50)

    def game_over1(self):
        over = myfont.render("GAME OVER1", 1,(255,0,0))
        screen.blit(over, (55, 55))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            pygame.display.update()
            clock.tick(50)

    def draw_food(self):
        pygame.draw.rect(screen, (255, 255, 255), self.foods)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_UP and self.dirs != 0:
                        self.dirs = 2
                    elif event.key == K_DOWN and self.dirs != 2:
                        self.dirs = 0
                    elif event.key == K_LEFT and self.dirs != 1:
                        self.dirs = 3
                    elif event.key == K_RIGHT and self.dirs != 3:
                        self.dirs = 1



            screen.fill((0,0,0))
            clock.tick(20)

            #self.collide_self()

            self.snakelen = len(self.snakex) - 1

            #ASSIGN NEW DESTINATION PER RECT
            while self.snakelen >= 1:
                self.snakex[self.snakelen] = self.snakex[self.snakelen - 1];
                self.snakey[self.snakelen] = self.snakey[self.snakelen - 1];
                self.snakelen -= 1
            self.wall()

            # MOVE
            if self.dirs == 0:
                self.snakey[0] += 5
            elif self.dirs == 1:
                self.snakex[0] += 5
            elif self.dirs == 2:
                self.snakey[0] -= 5
            elif self.dirs == 3:
                self.snakex[0] -= 5

            #DRAW SNAKE
            for i in range(0, len(self.snakex)):
                self.snake = pygame.Rect(self.snakex[i], self.snakey[i], self.snake_width, self.snake.height)
                self.eat()
                pygame.draw.rect(screen, (255, 255, 255), self.snake)


            self.draw_food()

            #SCORE
            score = myfont.render(str(self.cnt), False, (222,222,222))
            screen.blit(score, (10,10))

            pygame.display.flip()

app = Snake()
app.run()
