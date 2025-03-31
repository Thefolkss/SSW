import pygame

# C
C_WHITE = (255, 255, 255)
C_GRAY = (128, 128, 128)
C_GREEN = (161, 251, 142)
C_BLUE = (0, 12, 123)
C_GREEN2 = (24, 62, 12)

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

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 00,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
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
# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
