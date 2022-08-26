import pygame
from random import randint
from paths import the_path


class Enemy(pygame.sprite.Sprite):
    def __init__(self, the_type):
        super().__init__()
        if the_type == 'Cyborg':
            enemy_1 = pygame.image.load(the_path + "/new graphics/enemy run/run1.png").convert_alpha()
            enemy_2 = pygame.image.load(the_path + "/new graphics/enemy run/run2.png").convert_alpha()
            enemy_3 = pygame.image.load(the_path + "/new graphics/enemy run/run3.png").convert_alpha()
            enemy_4 = pygame.image.load(the_path + "/new graphics/enemy run/run4.png").convert_alpha()
            enemy_5 = pygame.image.load(the_path + "/new graphics/enemy run/run5.png").convert_alpha()
            enemy_6 = pygame.image.load(the_path + "/new graphics/enemy run/run6.png").convert_alpha()

            enemy_1 = pygame.transform.scale(enemy_1, (75, 100))
            enemy_2 = pygame.transform.scale(enemy_2, (75, 100))
            enemy_3 = pygame.transform.scale(enemy_3, (75, 100))
            enemy_4 = pygame.transform.scale(enemy_4, (75, 100))
            enemy_5 = pygame.transform.scale(enemy_5, (75, 100))
            enemy_6 = pygame.transform.scale(enemy_6, (75, 100))

            self.enemy_run = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6]

            killed_1 = pygame.image.load(the_path + "/new graphics/enemy killed/killed1.png").convert_alpha()
            killed_2 = pygame.image.load(the_path + "/new graphics/enemy killed/killed2.png").convert_alpha()
            killed_3 = pygame.image.load(the_path + "/new graphics/enemy killed/killed3.png").convert_alpha()
            killed_4 = pygame.image.load(the_path + "/new graphics/enemy killed/killed4.png").convert_alpha()
            killed_5 = pygame.image.load(the_path + "/new graphics/enemy killed/killed5.png").convert_alpha()
            killed_6 = pygame.image.load(the_path + "/new graphics/enemy killed/killed6.png").convert_alpha()

            killed_1 = pygame.transform.scale(killed_1, (75, 100))
            killed_2 = pygame.transform.scale(killed_2, (75, 100))
            killed_3 = pygame.transform.scale(killed_3, (75, 100))
            killed_4 = pygame.transform.scale(killed_4, (75, 100))
            killed_5 = pygame.transform.scale(killed_5, (75, 100))
            killed_6 = pygame.transform.scale(killed_6, (75, 100))

            self.enemy_killed = [killed_1, killed_2, killed_3, killed_4, killed_5, killed_6]
            self.HP = 1
            self.speed = 3

        else:
            enemy_1 = pygame.image.load(the_path + "/new graphics/stronger enemy run/enemy1.png").convert_alpha()
            enemy_2 = pygame.image.load(the_path + "/new graphics/stronger enemy run/enemy2.png").convert_alpha()
            enemy_3 = pygame.image.load(the_path + "/new graphics/stronger enemy run/enemy3.png").convert_alpha()
            enemy_4 = pygame.image.load(the_path + "/new graphics/stronger enemy run/enemy4.png").convert_alpha()

            enemy_1 = pygame.transform.scale(enemy_1, (75, 100))
            enemy_2 = pygame.transform.scale(enemy_2, (75, 100))
            enemy_3 = pygame.transform.scale(enemy_3, (75, 100))
            enemy_4 = pygame.transform.scale(enemy_4, (75, 100))

            self.enemy_run = [enemy_1, enemy_2, enemy_3, enemy_4]

            killed_1 = pygame.image.load(the_path + "/new graphics/stronger enemy killed/killed1.png").convert_alpha()
            killed_2 = pygame.image.load(the_path + "/new graphics/stronger enemy killed/killed2.png").convert_alpha()
            killed_3 = pygame.image.load(the_path + "/new graphics/stronger enemy killed/killed3.png").convert_alpha()
            killed_4 = pygame.image.load(the_path + "/new graphics/stronger enemy killed/killed4.png").convert_alpha()
            killed_5 = pygame.image.load(the_path + "/new graphics/stronger enemy killed/killed5.png").convert_alpha()
            killed_6 = pygame.image.load(the_path + "/new graphics/stronger enemy killed/killed6.png").convert_alpha()

            killed_1 = pygame.transform.scale(killed_1, (75, 100))
            killed_2 = pygame.transform.scale(killed_2, (75, 100))
            killed_3 = pygame.transform.scale(killed_3, (75, 100))
            killed_4 = pygame.transform.scale(killed_4, (75, 100))
            killed_5 = pygame.transform.scale(killed_5, (75, 100))
            killed_6 = pygame.transform.scale(killed_6, (75, 100))

            self.enemy_killed = [killed_1, killed_2, killed_3, killed_4, killed_5, killed_6]
            self.HP = 2
            self.speed = 1

        self.type = the_type
        self.killed = False
        self.index = 0
        self.end = False
        self.index_killd = 0
        self.image = self.enemy_run[self.index]
        random = randint(0, 1)

        if random == 0:
            self.rect = self.image.get_rect(midbottom=(randint(1000, 1200), 375))
        else:
            self.rect = self.image.get_rect(midbottom=(randint(1000, 1200), 475))

    def enemy_running(self):
        if not self.killed:
            self.rect.left -= self.speed

    def animation(self, the_player):
        if not self.killed:
            self.index += 0.1
            if self.index >= len(self.enemy_run):
                self.index = 0
            self.image = self.enemy_run[int(self.index)]

        else:
            self.index_killd += 0.2
            if self.index_killd >= len(self.enemy_killed):
                self.kill()
                if the_player.sprite.my_speed < the_player.sprite.max_speed:
                    the_player.sprite.my_speed += 0.1
                if self.type == 'Cyborg':
                    the_player.sprite.num_of_kills += 1
                else:
                    the_player.sprite.num_of_kills += 2
            else:
                self.image = self.enemy_killed[int(self.index_killd)]

    def death(self, the_player):
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollide(self, the_player, False) and keys[pygame.K_SPACE] \
                and not the_player.sprite.attacking:
            self.HP -= 1
            the_player.sprite.attacking = True
            if self.HP == 0:
                self.killed = True

    def update(self, the_player):
        self.enemy_running()
        self.animation(the_player)
        self.death(the_player)
