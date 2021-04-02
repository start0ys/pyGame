import pygame

pygame.init()   #초기화 (반드시 필수 무조건)

# 화면 크기 설정
screen_width = 480 #화면 가로크기
screen_height = 640 #화면 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("시작")  #게임이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/Administrator/Desktop/파이썬/Game/background.png")
#C:\Users\Administrator\Desktop\파이썬\Game\background.png 
#copy path로 불러온 주소는 이것인데 \를 사용하면 안되기때문에 /로 바꿔준다


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤틈가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    #screen.fill((0,0,255))  #배경 이미지를 불러오지않고 배경을 색칠하는 방법
    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임화면을 while문안에서 계속 다시그려서 유지시키기


# pygame 종료
pygame.quit()