import pygame
from random import * 
#####################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()   

# 화면 크기 설정
screen_width = 480 #화면 가로크기
screen_height = 640 #화면 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("시작")  #게임이름

# FPS
clock = pygame.time.Clock()
#######################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표 폰트 등)

# 배경설정
background = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/background.png" )#배경 설정

# 캐릭터 설정
character = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/정신이 캐릭터2.png")
character_size = character.get_rect().size #캐릭터 이미지 크기를 구해옴
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는곳에 위치
character_y_pos = screen_height - character_height # 화면 세로의 가장 아래 해당하는 곳에 위치

# 똥 설정
enemy = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/똥.png")
enemy_size = enemy.get_rect().size #똥 이미지 크기를 구해옴
enemy_width = enemy_size[0] #똥 가로크기
enemy_height = enemy_size[1] #똥 세로크기
enemy_x_pos = randrange(0, screen_width - enemy_width) # 똥의 가로위치는 랜덤으로 선정

enemy_y_pos = 0 # 똥은 처음에 맨위에 서 떨어진다



# 이동할 좌표
to_x = 0
to_y = 0

# 이동 스피드
mv_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 80) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 7

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

# 승리 패배 여부
Win_lose = 0

##############여기도 무조건###########################
# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤틈가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌렸을떄 작동
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= mv_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += mv_speed

        if event.type == pygame.KEYUP: # 키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    to_y += 0.3 # 똥 내려오는 속도
   
    


    # 3. 게임 캐릭터 위치 정의
    # 캐릭터 위치 정의
    character_x_pos += to_x

    #똥위치 정의
    enemy_y_pos += to_y
    

    # 캐릭터 경계값처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 똥 경계값 처리
    if enemy_y_pos < 0 :
        enemy_y_pos = 0
    elif enemy_y_pos > screen_height - enemy_height: #똥이 바닥까지 내려오면 다시 맨위로 올라가게하기
        enemy_y_pos = 0 
        to_y = 0 # 똥이 바닥에 내려오면 똥 내려오는 속도 초기화
        enemy_x_pos = randrange(0, screen_width - enemy_width) # 똥이 바닥에 내려오면 다음 새로운똥은 랜덤한 위치에서 떨어짐

   
    # 4. 충돌 처리
    # 캐릭터 정보 정의
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 똥 정보 정의
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect): # 캐릭터와 똥이 충돌했때
        running = False # 게임종료
        Win_lose = 1 # 똥을 피하지 못해 패배


    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # 경과 시간(ms)을 1000으로 나누어 초(s)단위로 변경

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # render 뒤에 는 (출력할 글자, True, 글자 색상)

    # 만약 시간이 0 이하이면 게임종료
    if total_time - elapsed_time <= 0:
        running = False
        Win_lose = 2 # 제한시간동안 똥을 피해 승리
    
    
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy , (enemy_x_pos, enemy_y_pos)) # 똥그리기
    screen.blit(timer, (430,10)) # 타이머 그리기
   
    #############무조건#####################
    pygame.display.update() # 게임화면을 while문안에서 계속 다시그려서 유지시키기

# 게임 승리 여부 문구
if Win_lose == 1: # 게임 패배시
    Game_Over = game_font.render("Game Over", True, (255,0,0))
    screen.blit(Game_Over, (95 , 270)) #중앙 좌표
    pygame.display.update() # 게임이 종료되어 while문 밖에 나왔을떄 Game Over를 업데이트

if Win_lose == 2: # 게임 승리시
    Game_Over = game_font.render("Winner", True, (255,0,0))
    screen.blit(Game_Over, (145 , 270)) #중앙 좌표
    pygame.display.update() # 게임이 종료되어 while문 밖에 나왔을떄 Game Over를 업데이트

# 종료 딜레이
pygame.time.delay(2000) # 종료 후 2초간 딜레이

# pygame 종료
pygame.quit()