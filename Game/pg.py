import pygame
#####################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()   

# 화면 크기 설정
screen_width = 640 #화면 가로크기
screen_height = 480 #화면 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("시작")  #게임이름

# FPS
clock = pygame.time.Clock()
#######################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표 폰트 등)

# 배경 및 무대 설정
background = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트배경.png") 
stage = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트무대.png") 

# 캐릭터 설정
character = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트캐릭터.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width - character_width 
character_y_pos = screen_height - character_height - 50

# 공 이미지 설정
ball_images = [
    pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트공1.png"),
    pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트공2.png"),
    pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트공3.png"),
    pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트공4.png") ]

# 공 크기에 따른 최초 스피드
ball_speed_y = [ -18, -15, -12, -9] 

# 공 설정
balls = []

balls.append({
  "pos_x" : 50, #공의 x좌표
  "pos_y" : 50,  #공의 y좌표
  "img_idx" : 0, # 공의 이미지 인덱스
  "to_b_x" : 3, # x축 이동방향
  "to_b_y" : -6, # y축 이동방향
  "fst_speed" : ball_speed_y[0] }) # y 최초속도


# 무기 설정
weapon = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/프로젝트무기.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = character_x_pos
weapon_y_pos = character_y_pos




# 제거 변수
ball_rv = -1
weapon_rv = -1

# 이동좌표
to_c_x = 0

# 이동속도
mv_speed = 5





# 무기 여러개 사용
weapons = [] #######################################################################


##############여기도 무조건###########################
# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤틈가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키보드 눌렀을때
            if event.key == pygame.K_LEFT: # 왼쪽 눌렀을떄
                to_c_x -= mv_speed
               
            elif event.key == pygame.K_RIGHT: # 오른쪽 눌렀을때
                to_c_x += mv_speed
              
            elif event.key == pygame.K_UP:        # 스페이스 눌렀을때
                weapon_x_pos = character_x_pos + 20 # 캐릭터 가운데에서 나오게하기위해 +20으로 위치 수정
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])  ##################################################
            
        if event.type == pygame.KEYUP: # 키보드 떼면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_c_x = 0
        
      
            
    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_c_x 

    

 
    # 캐릭터 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    weapons = [ [w[0],w[1] - 10] for w in weapons]

    # 공위치 정의

    for ball_idx , ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #공의 경계값 처리
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width: # 왼쪽 끝 or 오른쪽끝 경계 충돌하면
            ball_val["to_b_x"] = -ball_val["to_b_x"]   # 공의  가로 진행방향 반대
        if ball_pos_y > screen_height - 50 - ball_height: # 공이 땅에 충돌하면
            ball_val["to_b_y"] = ball_val["fst_speed"]  # 땅에서 최초 속도로 튕겨나간다
        else:
            ball_val["to_b_y"] += 0.5  #점점 속도가낮아지다가 0 지점에서떨어진다

        #공의 위치변화 적용
        ball_val["pos_x"] += ball_val["to_b_x"]
        ball_val["pos_y"] += ball_val["to_b_y"]





 
    # 4. 충돌 처리
    
    #캐릭터 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

  
    #공 정보 업데이트
    for b_idx , b_val in enumerate(balls):
        b_img_idx = b_val["img_idx"]
        ball_pos_x = b_val["pos_x"]
        ball_pos_y = b_val["pos_y"]
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        
        if ball_rect.colliderect(character_rect): # 공과 캐릭터가 충돌했을때
            pass
            #running = False
        
        #무기 정보 업데이트
        for w_idx , w_val in enumerate(weapons):
            weapon_x_pos = w_val[0]
            weapon_y_pos = w_val[1]
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            if weapon_rect.colliderect(ball_rect):  #공과 무기가 충돌했을떄
                ball_rv = b_idx # 공 제거 변수에 공 인덱스를 저장
                weapon_rv = w_idx # 무기 제거 변수에 무기 인덱스를 저장
                 
                if b_img_idx < 3: # 공을 4개까지 생성
                    #현재 공 크기 정보
                    ball_width = ball_size[0]
                    ball_height = ball_size[1]
                    # 나눠지는 작은공 정보
                    small_ball_size = ball_images[b_img_idx+1].get_rect().size
                    small_ball_width = small_ball_size[0]
                    small_ball_height = small_ball_size[1]
                    # 오른쪽 작은공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #작은공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),  #작은공의 y좌표
                        "img_idx" : b_img_idx + 1, # 공의 이미지 인덱스
                        "to_b_x" : +3, # x축 이동방향
                        "to_b_y" : -6, # y축 이동방향
                        "fst_speed" : ball_speed_y[b_img_idx+1] }) # y 최초속도

                    # 왼쪽 작은공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #작은공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),  #작은공의 y좌표
                        "img_idx" : b_img_idx + 1, # 공의 이미지 인덱스
                        "to_b_x" : -3, # x축 이동방향
                        "to_b_y" : -6, # y축 이동방향
                        "fst_speed" : ball_speed_y[b_img_idx+1] }) # y 최초속도
                
                break
        
        if ball_rv > -1:         # 안덱스는 0부터시작 0,1,2...
            del balls[b_idx]     # 공 제거
            ball_rv = -1         # 제거변수 초기화

        if weapon_rv > -1:       
            del weapons[w_idx]   # 무기제거
            weapon_rv = -1






 
    # 5. 화면에 그리기

    screen.blit(background, (0 , 0))
   
    for weapon_x_pos, weapon_y_pos in weapons:    
    
        screen.blit(weapon, (weapon_x_pos , weapon_y_pos))
    
    for idx , val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x , ball_pos_y))

    screen.blit(stage, (0 , 430))
    screen.blit(character, (character_x_pos , character_y_pos))

       
    #############무조건#####################
    pygame.display.update() # 게임화면을 while문안에서 계속 다시그려서 유지시키기
    



# pygame 종료
pygame.quit()