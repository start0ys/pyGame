import pygame

pygame.init()   #초기화 (반드시 필수 무조건)

# 화면 크기 설정
screen_width = 480 #화면 가로크기
screen_height = 640 #화면 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("시작")  #게임이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/background.png")
#C:\Users\Administrator\Desktop\파이썬\Game\background.png 
#copy path로 불러온 주소는 이것인데 \를 사용하면 안되기때문에 /로 바꿔준다

# 캐릭터(스프라이트) 불러오기 
character =  pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/정신이 캐릭터2.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# NPC만들기
NPC =  pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/NPC.png")
NPC_size = NPC.get_rect().size # 이미지의 크기를 구해옴
NPC_width = NPC_size[0] # 캐릭터의 가로크기
NPC_height = NPC_size[1] # 캐릭터의 세로크기
NPC_x_pos = (screen_width / 2) - (NPC_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
NPC_y_pos = (screen_height / 2) - (NPC_height / 2) # 화면 세로 크기 가장 아래에 해당하는곳에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 80) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 7

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    for event in pygame.event.get(): # 어떤 이벤틈가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
 
    character_x_pos += to_x * dt # 현재 캐릭터의 위치 좌표가 키보드이벤트로 발생한 가로위치를 더 해서 변경
    character_y_pos += to_y * dt # 현재 캐릭터의 위치 좌표가 키보드이벤트로 발생한 세로위치를 더 해서 변경
    
    # 가로 경계값처리
    if character_x_pos < 0: 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0: 
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect() # 캐릭터의 정보를 정의
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    NPC_rect = NPC.get_rect() # NPC 정보를 정의
    NPC_rect.left = NPC_x_pos
    NPC_rect.top = NPC_y_pos


    # 충돌 체크
    if character_rect.colliderect(NPC_rect): #캐럭터가 NPC와 충돌하면 게임 종료 
        running = False

    
    
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # 경과 시간(ms)을 1000으로 나누어 초(s)단위로 변경

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # render 뒤에 는 (출력할 글자, True, 글자 색상)

    # 만약 시간이 0 이하이면 게임종료
    if total_time - elapsed_time <= 0:
        running = False
    
    
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(NPC, (NPC_x_pos,NPC_y_pos)) # NPC 그리기
    screen.blit(timer, (430,10)) # 타이머 그리기
     

    pygame.display.update() # 게임화면을 while문안에서 계속 다시그려서 유지시키기


Game_Over = game_font.render("Game Over", True, (255,0,0))
screen.blit(Game_Over, (95 , 270)) #중앙 좌표
pygame.display.update() # 게임이 종료되어 while문 밖에 나왔을떄 Game Over를 업데이트

# 종료 대기
pygame.time.delay(2000) # 2ch 정도 대기 (ms)

# pygame 종료
pygame.quit()