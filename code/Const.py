import pygame

# C
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_GREEN = (161, 251, 142)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Player1Shot': 2,
    'Player2': 3,
    'Player2Shot': 2,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 80,
    'Enemy1Shot': 1,
    'Enemy2': 100,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 200,
}

# M
MENU_OPTION = ('NOVO JOGO - 1P',
               'NOVO JOGO - 2P COOPERATIVO',
               'NOVO JOGO- 2P COMPETITIVO',
               'PLACAR',
               'SAIR')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_KP0}
#S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
