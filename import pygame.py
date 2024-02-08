import pygame
import math

pygame.init()

screen = pygame.display.set_mode((700, 400))
screen_width = 700
# get clock
clock = pygame.time.Clock()
fps = 60

running = True
pygame.display.set_caption("Victor and Flourishing Bros")

icon = pygame.image.load("Blue and White Gradient Tech Instagram Post.png")
pygame.display.set_icon(icon)

#player
playerX = 240
playerY = 280

playerimg = pygame.image.load("New Piskel run 2-1.png (1).png")

standingimage  = pygame.transform.scale(playerimg, (60, 60))

def player(playerX,playerY):
    screen.blit(standingimage, (playerX, playerY))

#motion var
playerX_change = 0

#scrolling background has effect on X
scroll = 0
scroll -= 5

bg = pygame.image.load("Lbg.jpg").convert()




# main game loop
while running :
    clock.tick(fps)

    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
        if event.type == pygame.KEYUP:
            playerX_change = 0

# bg loop
    

    bg_width = bg.get_width()

    tiles = math.ceil(screen_width / bg_width) +1

    for i in range (0, tiles):
        screen.blit(bg, (i *bg_width + scroll, 0))


    if abs(scroll) > bg_width:
        scroll = 0


    playerX += playerX_change
    player(playerX, playerY)  



    pygame.display.update()

    