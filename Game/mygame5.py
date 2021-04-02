import pygame
from random import *
#####################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()   

# 화면 크기 설정
screen_width = 640 #화면 가로크기
screen_height = 720 #화면 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("시작")  #게임이름

# FPS
clock = pygame.time.Clock()
#######################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표 폰트 등)

#게임 무대 설정
background = pygame.image.load("Game/배경.png")
stage1 = pygame.image.load("Game/내골대.png")
#상대 골대 다르게 설정
stage2 = pygame.image.load("Game/상대골대2.png")
stage2_size = stage2.get_rect().size
stage2_width = stage2_size[0]
stage2_height = stage2_size[1]
stage2_x_pos = 560
stage2_y_pos = 0


#캐릭터 설정
character = pygame.image.load("Game/내캐릭터.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos =  (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - 45

#공 설정
ball = pygame.image.load("Game/내공.png")
ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_x_pos =  randrange(0,571)
ball_y_pos =  60


#폰트 추가
game_font = pygame.font.Font(None , 50)



# 캐릭터 이동좌표
to_c_x =0
# 공의 자동 이동좌표
to_b_x = 5
to_b_y = 10
# 스코어
my_score = 0
com_score = 0

##############여기도 무조건###########################
# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤틈가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_c_x -= 10
            elif event.key == pygame.K_RIGHT:
                to_c_x += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_c_x = 0


    # 3.  위치 정의
    character_x_pos += to_c_x
    ball_x_pos += to_b_x
    ball_y_pos += to_b_y
    # 경계값 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if ball_x_pos < 0 or ball_x_pos > screen_width - ball_width: # 공이 좌우 벽에 충돌할떄
        to_b_x = - to_b_x

    if ball_y_pos < 20 : #공이 상대골대 라인을 제외한 천장에 충돌할때
        to_b_y = - to_b_y
    
    if ball_y_pos > screen_height - ball_height - 20 : #공이 바닥에 충돌할때
        # 공초기화
        ball_x_pos = randrange(0,571) 
        ball_y_pos = 60
        
        com_score += 1 # 상대 스코어 1점추가
        if my_score < 2 and com_score < 2:
            goal1 = game_font.render("Goal",True, (255,255,255))
            screen.blit(goal1, ((screen_width / 2) - 50 , (screen_height / 2) - 50 )) #중앙 위치잡아주기
            pygame.display.update()
            pygame.time.delay(2000)


    # 4. 충돌 처리

    # 캐릭터 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 공 정보 업데이트
    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    #상대 골대 정보 업데이트
    stage2_rect = stage2.get_rect()
    stage2_rect.left = stage2_x_pos
    stage2_rect.top = stage2_y_pos

    if character_rect.colliderect(ball_rect): #캐릭터와 공이 충돌했을때
        to_b_y = -to_b_y

    if ball_rect.colliderect(stage2_rect): #공과 상대 골대가 충돌했을때   
        # 공초기화
        ball_x_pos = randrange(0,571) 
        ball_y_pos = 60
        
        my_score += 1 # 내스코어 1점 추가
        if my_score < 2 and com_score < 2:
            goal1 = game_font.render("Goal",True, (255,255,255))
            screen.blit(goal1, ((screen_width / 2) - 50 , (screen_height / 2) - 50 ))
            pygame.display.update()
            pygame.time.delay(2000)
    
    # 점수판 추가
    score = game_font.render("{0} : {1}".format(my_score,com_score), True , (0,0,0))
    
 
    if my_score == 2 or com_score == 2:  # 상대 점수가 5점이되거나 내점수가 5점이되면 게임종료
        running = False
        break

    
    # 5. 화면에 그리기
    screen.blit(background, (0 , 0))
    screen.blit(stage1, (0,700))
    screen.blit(stage2, (560,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(ball, (ball_x_pos,ball_y_pos))
    screen.blit(score, (5,5))
    #############무조건#####################
    pygame.display.update() # 게임화면을 while문안에서 계속 다시그려서 유지시키기

if my_score == 2:
    Win = game_font.render("Win",True,(255,0,0))
    screen.blit(Win, ((screen_width / 2) - 50 , (screen_height / 2) - 50 ))
    pygame.display.update()

if com_score == 2:
    Lose = game_font.render("Lose",True,(255,0,0))
    screen.blit(Lose, ((screen_width / 2) - 50 , (screen_height / 2) - 50 ))
    pygame.display.update()
# 최종 스코어 추가
score = game_font.render("{0} : {1}".format(my_score,com_score), True , (255,255,255))
screen.blit(score, ((screen_width / 2) - 50 , (screen_height / 2) - 80 ))
pygame.display.update()

pygame.time.delay(2000)

# pygame 종료
pygame.quit()