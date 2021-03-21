# Pygame Crash Course -- PYTHON + GAME! 
import pygame
import sys
#abcd
pygame.init() # initialize all the pygame's functions and datas

screen = pygame.display.set_mode((1200, 700)) #screen instance
                                              #pass in a tuple here
pikachu = pygame.image.load("images/pikachu.png") #return an image instance
pikachu = pygame.transform.scale(pikachu, (100, 100)) 
pikachu_rect = pikachu.get_rect(topleft = (100, 560))
goomba = pygame.image.load("images/goomba.png")
goomba = pygame.transform.scale(goomba, (64,64))
goomba_rect = goomba.get_rect(topleft = (1000, 596))
bg = pygame.image.load("images/bg2.png")
floor = pygame.image.load("images/floor.png")

# loading font
font = pygame.font.Font("font/font3.otf", 36) # font instance
game_over_text = font.render("GAME OVER", True, (0,0,0)) # text isntance 
welcome_text = font.render("Welcome to my world", True, (123,25,111))

# loading sounds
gameover_sound = pygame.mixer.Sound("sound/gameover.mp3") #sound 
gameovered = 0
hit_sound = pygame.mixer.Sound("sound/hit2.mp3")

# list
animation_list = [] 
animation_list.append(pygame.image.load("images/1.png"))
animation_list.append(pygame.image.load("images/2.png"))
animation_list.append(pygame.image.load("images/3.png"))
animation_list.append(pygame.image.load("images/4.png"))
for i, animation in enumerate(animation_list):
    animation_list[i] = pygame.transform.scale(animation_list[i], (100,100))
    # rescaled all the images inside of this list to be 100, 100
count = 0

while True: 
    events = pygame.event.get()
    for event in events: # -> this will return a list []
        if event.type == pygame.QUIT:
            sys.exit()
        #ad 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # user pressed the key "A"
                count += 1
                if count >= 4:
                    count = 0
                if pikachu_rect.x >= 0:
                    pikachu_rect.x -= 3
            if event.key == pygame.K_d:
                count += 1
                if count >= 4:
                    count = 0
                if pikachu_rect.x <= 1100:
                    pikachu_rect.x += 10
            if event.key == pygame.K_SPACE:
                pikachu_rect.y -= 10 
            
            # we only want it to move whden we pressed "A" and "D"

    goomba_rect.x -= 3
    screen.blit(bg, (0, 0))
    screen.blit(floor, (0, 660))
    screen.blit(goomba, goomba_rect) #goomba_rect.x and goomba_rect.y
    screen.blit(animation_list[int(count)], pikachu_rect) #method of screen instance 
    screen.blit(welcome_text, (300, 100))
    if pikachu_rect.colliderect(goomba_rect) == True:
        print("Game over!")
        gameovered += 1
        hit_sound.play()
        if gameovered == 1: 
            gameover_sound.play()
        screen.blit(game_over_text, (500, 300))
        # sys.exit()

    pygame.display.update() #updates the screen