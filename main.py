# importing the library
import math

import pygame
import random

# initialization
pygame.init()

# screen display
screen = pygame.display.set_mode((800, 600))

# Set icon & Name
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load("chicken.png")
pygame.display.set_icon(icon)

# Background image
background = pygame.image.load("farmBG.png")

# player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

# fox
foxImg = pygame.image.load("fox.png")
foxX = random.randint(0, 736)
foxY = random.randint(50, 100)
foxX_change = 1
foxY_change = 2

# balloon
balloonImg = pygame.image.load('balloon.png')
balloonX = 0
balloonY = 480
balloonX_change = 0
balloonY_change = 5
balloon_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def fox(x, y):
    screen.blit(foxImg, (x, y))


def fire_balloon(x, y):
    global balloon_state
    balloon_state = "fire"
    screen.blit(balloonImg, (x + 16, y + 16))


# collision
def iscollision(foxX, foxY, balloonX, balloonY):
    distance = math.sqrt(math.pow(foxX - balloonX, 2) + math.pow(foxY - balloonY, 2))
    if distance < 25:
        return True
    else:
        return False


# game loop
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if balloon_state == "ready":
                    balloonX = playerX
                    fire_balloon(balloonX, balloonY)
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # setting boundaries for the player
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    foxX += foxX_change
    if foxX <= 0:
        foxX_change = 2
        foxY += foxY_change
    if foxX >= 736:
        foxX_change = -2
        foxY += foxY_change

    # balloon movement
    if balloonY <= 0:
        balloonY = 480
        balloon_state = "ready"
    if balloon_state == "fire":
        fire_balloon(balloonX, balloonY)
        balloonY -= balloonY_change

    player(playerX, playerY)
    fox(foxX, foxY)
    pygame.display.update()

# collision impact
collision = iscollision(foxX, foxY, balloonX, balloonY)
if collision:
    balloonY = 400
    balloon_state = "ready"
    foxX = random.randint(0, 736)
    foxY = random.randint(50, 150)
