# %%
import pygame
import sys
fp = "C:/Users/user/Desktop/python's_stuff/visualstudio/Contra/"
fb = "C:/Users/user/Desktop/python's_stuff/visualstudio/mario/"
pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
bg = pygame.image.load("images/bg2_extended.png")
bg_x = 0
floor = pygame.image.load("images/floor_extended.png")
floor_x = 0 
image_list = []
# image_list.append(pygame.image.load("images/pikachu.png"))
image_list.append(pygame.image.load("images/1.png"))
image_list.append(pygame.image.load("images/2.png"))
image_list.append(pygame.image.load("images/3.png"))
image_list.append(pygame.image.load("images/4.png"))
image_list.append(pygame.image.load("images/5.png"))
image_list.append(pygame.image.load("images/6.png"))
image_list.append(pygame.image.load("images/7.png"))
for i, image in enumerate(image_list):
    image_list[i] = pygame.transform.scale(image, (100, 115))
player1_rect = image_list[0].get_rect(topleft = (10, 485))
# player1_rect = player1.get_rect(topleft = (10, 540))

current_step = 0
pressed_right = False
pressed_left = False
jumped = False
base_speed = 8  
velocity_k = 1.1
def event_handler():
    global pressed_left
    global current_step 
    global pressed_right
    global jumped 
    global floor_x
    global bg_x
    global base_speed
    global velocity_k
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pressed_right = True
                pressed_left = False
            if event.key == pygame.K_LEFT:
                pressed_left = True
                pressed_right = False
            if event.key == pygame.K_SPACE and player1_rect.y >=485:
                jumped = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pressed_right = False
            if event.key == pygame.K_LEFT:
                pressed_left = False
            if event.key == pygame.K_SPACE:
                jumped = False
                
    if bg_x <= -1200: 
        bg_x = 0
    if floor_x <= -1200:
        floor_x = 0
    if pressed_right == True:
        current_step += 0.1
        if current_step >= len(image_list):
            current_step = 0
        if player1_rect.x >= 584:
            bg_x -= 2
            floor_x -= 4
        else:
            player1_rect.x += 4
    elif pressed_left == True:
        current_step += 0.1
        if current_step >= len(image_list):
            current_step = 0
        if player1_rect.x >=5:
            player1_rect.x -= 4
    else:
        current_step = 0
    if jumped == True:  
        if player1_rect.y >= 300:
            player1_rect.y -= base_speed 
        else:
            jumped = False
    else:
        if player1_rect.y <485:
            player1_rect.y += base_speed 


while True:
    screen.blit(bg, (bg_x,0))   
    player1_rect = image_list[int(current_step)].get_rect(topleft= player1_rect.topleft)
    event_handler()
    screen.blit(image_list[int(current_step)], player1_rect)
    screen.blit(floor, (floor_x, 660))
    pygame.display.update()
    clock.tick(90)
# %%
# %%
