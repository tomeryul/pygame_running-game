import pygame
from random import choice
from character import Player
from enemy import Enemy
from sys import exit
from paths import the_path
Fps = 60

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("running game")
score_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
num_of_kills = 0
game_active = False

# ############## the background ########### #

beck_ground_surface = pygame.image.load(the_path + "/new graphics/background/Background.png").convert()
beck_ground_surface = pygame.transform.scale(beck_ground_surface, (1000, 300))
flore_surface = pygame.image.load(the_path + "/new graphics/background/road&lamps_pale.png").convert()
flore_surface = pygame.transform.scale(flore_surface, (1000, 1200))

# ######################################## #


# ################ Groups ################# #

# player group
player = pygame.sprite.GroupSingle()
player.add(Player())

# enemy group
Enemies_Group = pygame.sprite.Group()

# ######################################### #


# timer to spawn an enemy
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)


def collisions():
    for enemy in Enemies_Group.sprites():
        if enemy.rect.left <= 0:  # check if one of the enemies the went too left
            return False          # in order to check if the player went too left write: player.sprite.rect
    return True


def the_main_screen():
    screen.blit(flore_surface, (0, -700))
    screen.blit(beck_ground_surface, (0, 0))
    my_score = player.sprite.num_of_kills
    score_surf = score_font.render(f'score: {my_score}', False, 'Black')
    score_rect = score_surf.get_rect(center=(500, 20))
    pygame.draw.rect(screen, 'Pink', score_rect)
    screen.blit(score_surf, score_rect)
    return my_score


def set_end_screen():
    screen.fill('#606BFC')
    if num_of_kills > 0:
        score_surf = score_font.render(f"You're score was: {num_of_kills}", False, 'White')
    else:
        score_surf = score_font.render(f"Press space to start", False, 'White')
    score_rect = score_surf.get_rect(center=(500, 400))
    screen.blit(score_surf, score_rect)
    name_surf = score_font.render(f'PVZ killing game', False, 'White')
    name_rect = name_surf.get_rect(midbottom=(500, 100))
    screen.blit(name_surf, name_rect)
    man_stand = pygame.image.load(
        the_path + "/new graphics/new character/stand/stand.png").convert_alpha()
    man_character_end = pygame.transform.scale(man_stand, (200, 240))
    man_rect_end = man_character_end.get_rect(midbottom=(500, 350))
    screen.blit(man_character_end, man_rect_end)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    player.sprite.num_of_kills = 0
                    player.sprite.my_speed = 3
                    Enemies_Group.empty()

        if game_active:
            if event.type == obstacle_timer:
                Enemies_Group.add(Enemy(choice(['Cyborg', 'Cyborg', 'Cyborg', 'Drone'])))

    if game_active:

        # the background
        num_of_kills = the_main_screen()

        # the man on the screen
        player.draw(screen)
        player.update()

        # the enemy on the screen
        Enemies_Group.draw(screen)
        Enemies_Group.update(player)

        # check collisions
        game_active = collisions()

    else:
        set_end_screen()

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(Fps)
