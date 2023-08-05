import pygame
import random
import sys
import os
# 게임 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# 색깔 정의
WHITE = (255, 255, 255)

# 시계 설정
clock = pygame.time.Clock()
# 바닥 이미지 로드
floor_img = pygame.image.load(os.path.join("C:\Flappy Bird\FlappyResource", "floor.png"))
floor_img = pygame.transform.scale(floor_img, (floor_img.get_width() * 2, floor_img.get_height()))

# 백그라운드 이미지 로드
background_img = pygame.image.load(os.path.join("C:\Flappy Bird\FlappyResource", "back.png"))

# 새 이미지 로드
bird_img = pygame.image.load(os.path.join("C:\Flappy Bird\FlappyResource", "baid up_1.png"))
bird_rect = bird_img.get_rect()
# 게임 오버  이미지 로드
gameover_img = pygame.image.load(os.path.join("C:\Flappy Bird\FlappyResource", "gameover.png"))

# 파이프 이미지 로드 (상단과 하단 이미지로 나누기)
pipe_img = pygame.image.load(os.path.join("C:\Flappy Bird\FlappyResource", "pipe.png"))
pipe_top_img = pygame.transform.rotate(pipe_img, 180)
# 프로피버드 로고 이미지 로드
propybird_logo_img = pygame.image.load(os.path.join("C:\Flappy Bird\FlappyResource", "FlappyBird.png"))

# 레디 버튼 이미지 로드
ready_btn_img = pygame.image.load(os.path.join("C:\Flappy Bird\FlappyResource", "Ready.png"))
ready_btn_rect = ready_btn_img.get_rect()
ready_btn_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.6)
# 새의 초기 위치 설정
bird_x = 100
bird_y = SCREEN_HEIGHT // 2

# 새의 속도 설정
bird_speed = 0
gravity = 0.25
jump_strength = -4

# 파이프 변수 설정
pipe_width = 70
pipe_height = random.randint(150, 400)
pipe_gap = 150
pipe_x = SCREEN_WIDTH
pipe_y = random.randint(0, SCREEN_HEIGHT - pipe_gap)

# 바닥 변수 설정
floor_speed = 2
floor_x = 0

# 게임 오버 변수 설정
game_over = False

def reset_pipe():
    global pipe_height, pipe_y, pipe_x
    pipe_height = random.randint(150, 400)
    pipe_y = random.randint(0, SCREEN_HEIGHT - pipe_gap)
    pipe_x = SCREEN_WIDTH

def check_collision():
    if bird_rect.colliderect(pygame.Rect(pipe_x, 0, pipe_width, pipe_height)) or \
            bird_rect.colliderect(pygame.Rect(pipe_x, pipe_y + pipe_gap, pipe_width, SCREEN_HEIGHT)):
        return True
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return True
    return False

def game_over_screen():
    screen.blit(gameover_img, (SCREEN_WIDTH // 2 - gameover_img.get_width() // 2, SCREEN_HEIGHT // 2 - gameover_img.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)
# 게임 시작 화면

game_started = False  # Define the variable outside the function
def start_screen():
    global game_started  # Use the global variable inside the function
    while not game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_started = True

        for i in range(SCREEN_WIDTH // background_img.get_width() + 1):
            screen.blit(background_img, (i * background_img.get_width(), 0))
        screen.blit(propybird_logo_img, (SCREEN_WIDTH // 2 - propybird_logo_img.get_width() // 2, SCREEN_HEIGHT * 0.4))
        screen.blit(ready_btn_img, ready_btn_rect)
        screen.blit(floor_img, (0, SCREEN_HEIGHT - floor_img.get_height()))

    
        pygame.display.update()
        clock.tick(60)

# 게임 시작
def game_start():
    global game_started
    game_started = True

# ... (previous code) ...

# 게임 루프
while not game_over:
    if not game_started:
        start_screen()

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird_speed = jump_strength

    # 새의 위치 업데이트
    bird_speed += gravity
    bird_y += bird_speed
    bird_rect.topleft = (bird_x, bird_y)

    # 파이프의 위치 업데이트
    pipe_x -= 2
    if pipe_x + pipe_width < 0:
        reset_pipe()

    # 파이프의 y좌표 설정
    pipe_y = SCREEN_HEIGHT - pipe_height

    # 충돌 체크
    if check_collision():
        game_over = True

    # 배경 반복 그리기 (생략)

    for i in range(SCREEN_WIDTH // background_img.get_width() + 1):
        screen.blit(background_img, (i * background_img.get_width(), 0))

    # 화면 업데이트
    screen.blit(bird_img, bird_rect)
    screen.blit(pipe_top_img, (pipe_x, 0))
    screen.blit(pipe_img, (pipe_x, pipe_y + pipe_gap))
    screen.blit(floor_img, (0, SCREEN_HEIGHT - floor_img.get_height()))
    
    if game_over:  # Exit the game loop if game_over is True
        break
    
    pygame.display.update()
    # 게임 속도 조절
    clock.tick(60)

# 게임 종료
game_over_screen()
pygame.quit()
sys.exit()
