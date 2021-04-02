import pygame
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
stage2 = pygame.image.load("Game/상대골대2.png")

#캐릭터 설정
character = pygame.image.load("Game/내캐릭터.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos =  (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - 45

ball = pygame.image.load("Game/내공.png")






# 캐릭터 이동좌표
to_c_x =0

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


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_c_x

    # 경계값 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0 , 0))
    screen.blit(stage1, (0,700))
    screen.blit(stage2, (560,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    #############무조건#####################
    pygame.display.update() # 게임화면을 while문안에서 계속 다시그려서 유지시키기


# pygame 종료
pygame.quit()