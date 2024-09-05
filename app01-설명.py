import pygame

# Pygame 라이브러리를 초기화하여 사용할 준비를 함
pygame.init()

# 게임 창의 제목을 "Flappy Bird"로 설정
pygame.display.set_caption("Flappy Bird")

# 게임 화면의 크기를 (가로 288, 세로 512) 픽셀로 설정
screen_size = (288, 512)

# 설정된 크기의 게임 화면(창)을 생성하고, 'screen' 변수에 저장
screen = pygame.display.set_mode(screen_size)

# 게임 루프를 실행할지 여부를 결정하는 플래그 변수
running = True

# 메인 게임 루프. running이 True인 동안 반복됩니다.
while running:
    # Pygame의 이벤트 큐에서 발생한 모든 이벤트를 가져와 순회합니다.
    # 여기서 각 이벤트는 사용자의 입력이나 시스템 이벤트를 의미합니다.
    for event in pygame.event.get():
        # 만약 이벤트의 종류가 'QUIT' (창 닫기 버튼을 눌렀을 때)라면
        if event.type == pygame.QUIT:
            # 'running' 변수를 False로 설정하여 게임 루프를 종료합니다.
            running = False

    # 화면을 검은색으로 채웁니다 (RGB 값 (0, 0, 0)으로 채움)
    # 이 작업은 화면을 지워 이전 프레임에서 그려진 그래픽을 제거하고, 다음 프레임을 그릴 준비를 합니다.
    # 만약 화면을 지우지 않으면, 이전 프레임의 그래픽이 그대로 남아 있어 움직이는 객체가 지나간 자리에 잔상이 남거나, 그래픽이 겹쳐 보일 수 있습니다.
    screen.fill(0)

    # 위에서 준비한 모든 내용을 실제 게임 창에 보여줍니다.
    # Pygame은 더블 버퍼링을 사용하므로 화면 깜박임 없이 부드럽게 이미지를 갱신할 수 있습니다.
    pygame.display.flip()

# 게임이 종료되면, Pygame 라이브러리를 종료하여 모든 Pygame 모듈을 정리합니다.
pygame.quit()
