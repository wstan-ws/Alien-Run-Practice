import pygame
from sys import exit

# create display score function (method)
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = font_score.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 65))
    screen.blit(score_surface, score_rect)

# initialise pygame
pygame.init()

# creating and set width and height of display window
screen = pygame.display.set_mode((800, 400))
# create title of game (displayed on title bar of window)
pygame.display.set_caption("Alien Run")
# create clock to control framerate of game
clock = pygame.time.Clock()
# create font to display in game
font_title = pygame.font.Font("font/Pixeltype.ttf", 100)
font_instructions = pygame.font.Font("font/Pixeltype.ttf", 60)
font = pygame.font.Font("font/Pixeltype.ttf", 60)
font_score = pygame.font.Font("font/Pixeltype.ttf", 45)
# create game status
game_active = False
# create start time
start_time = 0

# Creating a regular surface and setting width and height of object
    # >>> test_surface = pygame.Surface((100, 200))
# Adding fill to display surface/object
    # >>> test_surface.fill("Red")
# Creating a regular surface object using a picture
# .convert() converts the image from to png to another type the is more compatible with python
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Creating a text surface (actual text, anti-aliasing, colour)
text_surface = font.render("Alien Run", False, (64, 64, 64))
text_rect = text_surface.get_rect(center = (400, 30))

# .convert_alpha() removes the weird black and white background from the image after .convert()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
# draw a rectangle around the player object and placing the rectangle on a specific position
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

text_title = font_title.render("Alien Run", False, (111, 196, 169))
text_title_rect = text_title.get_rect(center = (400, 70))

text_instructions = font_instructions.render("Press 'Space' to Start", False, (111, 196, 169))
text_instructions_rect = text_instructions.get_rect(center = (400, 350))

# draw all elements and update everything here
while True:
    
    # check for inputs
    for event in pygame.event.get():
        # check for close window input
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # check the position of mouse
            # >>> if event.type == pygame.MOUSEMOTION:
                # >>> print(event.pos)
        # check if mouse button is pressed
            # >>> if event.type == pygame.MOUSEBUTTONDOWN:
                # >>> print("mouse down")
        # check if mouse button is released
            # >>> if event.type == pygame.MOUSEBUTTONUP:
                # >>> print("mouse up")
        # check if a key is released
            # >>> if event.type == pygame.KEYUP:
                # >>> print("key up")
        
        if game_active:
            # check if a key is pressed
            if event.type == pygame.KEYDOWN:
                # check if space is pressed and if player is on ground
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            # player jumps when user clicks on player object
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if player and mouse collides and if player is on ground
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
        # at game over screen, check for space button pressed
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # reset snail position
                snail_rect.left = 800
                # start game status
                game_active = True
                # restart score
                start_time = int(pygame.time.get_ticks()/1000)
                 
    if game_active:
        # attaching object on window surface on specific positioning
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # drawing a rectangle
            # >>> pygame.draw.rect(screen, "#c0e8ec", text_rect)
        screen.blit(text_surface, text_rect)
        # drawing a line
            # >>> pygame.draw.line(screen, "Gold", (0, 0), pygame.mouse.get_pos(), 10)
        # drawing a circle
            # >>> pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))
        display_score()
        
        # moving the snail on screen to the left
        snail_rect.x -= 4
        # moving the snail back to right of screen when snail goes off screen on the left
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # creating gravity for falling player
        player_gravity += 1
        player_rect.y += player_gravity
        # creating ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        # placing the player object on the player rectangle position
        screen.blit(player_surface, player_rect)

        # creating collision between player and snail
        if snail_rect.colliderect(player_rect):
            game_active = False

        # adding user keyboard input
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")

        # checking for collision between rectangles
        # if player_rect.colliderect(snail_rect):
        #     print("collision")

        # checking if mouse collide on object
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     # checking which moouse button is pressed (left click, middle click, right click)
        #     print(pygame.mouse.get_pressed())
    else:
        screen.fill((94, 129, 162))        
        screen.blit(player_stand, player_stand_rect)
        screen.blit(text_title, text_title_rect)
        screen.blit(text_instructions, text_instructions_rect)

    # update display surface
    pygame.display.update()
    # set ceiling of 60fps
    clock.tick(60)