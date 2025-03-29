#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_GRAY, COLOR_GREEN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Clouds3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/MenuSound.wav')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "SPACE", COLOR_WHITE, ((WIN_WIDTH / 2), 60))
            self.menu_text(50, "SHOOTERS", COLOR_WHITE, ((WIN_WIDTH / 2), 95))
            self.menu_text(50, "WAR", COLOR_WHITE, ((WIN_WIDTH / 2), 130))
            self.menu_text(15, "By: Felipe 'Folks' Knaut", COLOR_WHITE, ((60), 10))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_GRAY, ((WIN_WIDTH / 2), 180 + 30 * i))


            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER KEY
                        return MENU_OPTION[menu_option]


            pygame.display.flip()

    # new
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
