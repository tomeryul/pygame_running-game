import pygame
from paths import the_path


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        man_walk_1 = pygame.image.load(the_path + "/new graphics/new character/run/run1.png").convert_alpha()
        man_walk_2 = pygame.image.load(the_path + "/new graphics/new character/run/run2.png").convert_alpha()
        man_walk_3 = pygame.image.load(the_path + "/new graphics/new character/run/run3.png").convert_alpha()
        man_walk_4 = pygame.image.load(the_path + "/new graphics/new character/run/run4.png").convert_alpha()
        man_walk_5 = pygame.image.load(the_path + "/new graphics/new character/run/run5.png").convert_alpha()
        man_walk_6 = pygame.image.load(the_path + "/new graphics/new character/run/run6.png").convert_alpha()
        man_stand = pygame.image.load(the_path + "/new graphics/new character/stand/stand.png").convert_alpha()

        man_walk_back_1 = pygame.image.load(
            the_path + "/new graphics/new character/run_backward/run1.png").convert_alpha()
        man_walk_back_2 = pygame.image.load(
            the_path + "/new graphics/new character/run_backward/run2.png").convert_alpha()
        man_walk_back_3 = pygame.image.load(
            the_path + "/new graphics/new character/run_backward/run3.png").convert_alpha()
        man_walk_back_4 = pygame.image.load(
            the_path + "/new graphics/new character/run_backward/run4.png").convert_alpha()
        man_walk_back_5 = pygame.image.load(
            the_path + "/new graphics/new character/run_backward/run5.png").convert_alpha()
        man_walk_back_6 = pygame.image.load(
            the_path + "/new graphics/new character/run_backward/run6.png").convert_alpha()

        man_attack_1 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack1.png").convert_alpha()
        man_attack_2 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack2.png").convert_alpha()
        man_attack_3 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack3.png").convert_alpha()
        man_attack_4 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack4.png").convert_alpha()
        man_attack_5 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack5.png").convert_alpha()
        man_attack_6 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack6.png").convert_alpha()
        man_attack_7 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack7.png").convert_alpha()
        man_attack_8 = pygame.image.load(
            the_path + "/new graphics/new character/player attack/attack8.png").convert_alpha()

        man_walk_1 = pygame.transform.scale(man_walk_1, (75, 100))
        man_walk_2 = pygame.transform.scale(man_walk_2, (75, 100))
        man_walk_3 = pygame.transform.scale(man_walk_3, (75, 100))
        man_walk_4 = pygame.transform.scale(man_walk_4, (75, 100))
        man_walk_5 = pygame.transform.scale(man_walk_5, (75, 100))
        man_walk_6 = pygame.transform.scale(man_walk_6, (75, 100))

        man_walk_back_1 = pygame.transform.scale(man_walk_back_1, (75, 100))
        man_walk_back_2 = pygame.transform.scale(man_walk_back_2, (75, 100))
        man_walk_back_3 = pygame.transform.scale(man_walk_back_3, (75, 100))
        man_walk_back_4 = pygame.transform.scale(man_walk_back_4, (75, 100))
        man_walk_back_5 = pygame.transform.scale(man_walk_back_5, (75, 100))
        man_walk_back_6 = pygame.transform.scale(man_walk_back_6, (75, 100))

        man_attack_1 = pygame.transform.scale(man_attack_1, (75, 100))
        man_attack_2 = pygame.transform.scale(man_attack_2, (75, 100))
        man_attack_3 = pygame.transform.scale(man_attack_3, (75, 100))
        man_attack_4 = pygame.transform.scale(man_attack_4, (75, 100))
        man_attack_5 = pygame.transform.scale(man_attack_5, (95, 100))
        man_attack_6 = pygame.transform.scale(man_attack_6, (95, 100))
        man_attack_7 = pygame.transform.scale(man_attack_7, (95, 100))
        man_attack_8 = pygame.transform.scale(man_attack_8, (75, 100))

        self.man_stand = pygame.transform.scale(man_stand, (75, 100))
        self.man_walk = [man_walk_1, man_walk_2, man_walk_3, man_walk_4, man_walk_5, man_walk_6]
        self.man_walk_back = [man_walk_back_1, man_walk_back_2, man_walk_back_3, man_walk_back_4,
                              man_walk_back_5, man_walk_back_6]
        self.man_attack = [man_attack_1, man_attack_2, man_attack_3, man_attack_4, man_attack_5, man_attack_6,
                           man_attack_7, man_attack_8]
        self.max_speed = 7
        self.num_of_kills = 0
        self.index = 0
        self.attacking_index = 0
        self.my_speed = 3
        self.attacking = False
        self.end = False
        self.image = self.man_walk[self.index]
        self.rect = self.image.get_rect(midbottom=(100, 375))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if not self.attacking:
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.left -= self.my_speed

            if keys[pygame.K_RIGHT] and self.rect.right < 1000:
                self.rect.left += self.my_speed

            if keys[pygame.K_DOWN] and self.rect.bottom == 375:
                self.rect.bottom = 475

            if keys[pygame.K_UP] and self.rect.bottom == 475:
                self.rect.bottom = 375

    def animation(self):
        keys = pygame.key.get_pressed()
        if not self.attacking:
            if keys[pygame.K_RIGHT]:
                self.index += 0.1
                if self.index >= len(self.man_walk):
                    self.index = 0
                self.image = self.man_walk[int(self.index)]

            elif keys[pygame.K_LEFT]:
                self.index += 0.1
                if self.index >= len(self.man_walk_back):
                    self.index = 0
                self.image = self.man_walk_back[int(self.index)]

            else:
                self.index = 0
                self.image = self.man_stand

        elif self.attacking:
            self.attacking_index += 0.3
            if self.attacking_index >= len(self.man_attack):
                self.attacking = False
                self.attacking_index = 0
            self.image = self.man_attack[int(self.attacking_index)]

    def update(self):
        self.player_input()
        self.animation()
