import pygame
import random
# from job import Job, sheriff, outlaw, deputy, renegade

screen_scale = 0.83333

pygame.init()
screen = pygame.display.set_mode((1920 * screen_scale, 1080 * screen_scale))
pygame.display.set_caption("BANG!")

image_scale = 0.5 * screen_scale

size_bg_w = screen.get_size()[0]
size_bg_h = screen.get_size()[1]

image_board0 = pygame.image.load("image/board/board0.png")
image_board1 = pygame.image.load("image/board/board1.png")
image_board2 = pygame.image.load("image/board/board2.png")
image_board3 = pygame.image.load("image/board/board3.png")
image_board4 = pygame.image.load("image/board/board4.png")
image_board5 = pygame.image.load("image/board/board5.png")
image_board6 = pygame.image.load("image/board/board6.png")
image_board7 = pygame.image.load("image/board/board7.png")

image_size_ws = []
image_size_ws.append(image_board0.get_rect().size[0])
image_size_ws.append(image_board1.get_rect().size[0])
image_size_ws.append(image_board2.get_rect().size[0])
image_size_ws.append(image_board3.get_rect().size[0])
image_size_ws.append(image_board4.get_rect().size[0])
image_size_ws.append(image_board5.get_rect().size[0])
image_size_ws.append(image_board6.get_rect().size[0])
image_size_ws.append(image_board7.get_rect().size[0])

image_size_hs = []
image_size_hs.append(image_board0.get_rect().size[1])
image_size_hs.append(image_board1.get_rect().size[1])
image_size_hs.append(image_board2.get_rect().size[1])
image_size_hs.append(image_board3.get_rect().size[1])
image_size_hs.append(image_board4.get_rect().size[1])
image_size_hs.append(image_board5.get_rect().size[1])
image_size_hs.append(image_board6.get_rect().size[1])
image_size_hs.append(image_board7.get_rect().size[1])

image_size_ws = [x * image_scale for x in image_size_ws]
image_size_hs = [x * image_scale for x in image_size_hs]

# 사이즈 변경
image_board0 = pygame.transform.scale(image_board0, (image_size_ws[0], image_size_hs[0]))
image_board1 = pygame.transform.scale(image_board1, (image_size_ws[1], image_size_hs[1]))
image_board2 = pygame.transform.scale(image_board2, (image_size_ws[2], image_size_hs[2]))
image_board3 = pygame.transform.scale(image_board3, (image_size_ws[3], image_size_hs[3]))
image_board4 = pygame.transform.scale(image_board4, (image_size_ws[4], image_size_hs[4]))
image_board5 = pygame.transform.scale(image_board5, (image_size_ws[5], image_size_hs[5]))
image_board6 = pygame.transform.scale(image_board6, (image_size_ws[6], image_size_hs[6]))
image_board7 = pygame.transform.scale(image_board7, (image_size_ws[7], image_size_hs[7]))


image_bullet_front = pygame.image.load("image/bullet/bullet_front.png")
image_bullet_back = pygame.image.load("image/bullet/bullet_back.png")

# 사이즈 변경
image_bullet_front = pygame.transform.scale(image_bullet_front, (\
  image_bullet_front.get_rect().size[0] * image_scale, image_bullet_front.get_rect().size[1] * image_scale))
image_bullet_back = pygame.transform.scale(image_bullet_back, (\
  image_bullet_back.get_rect().size[0] * image_scale, image_bullet_back.get_rect().size[1] * image_scale))

# 회전
image_bullet_front_down = pygame.transform.rotate(image_bullet_front, 145)
image_bullet_back_down = pygame.transform.rotate(image_bullet_back, 145)
image_bullet_front_up = pygame.transform.rotate(image_bullet_front, 325)
image_bullet_back_up = pygame.transform.rotate(image_bullet_back, 325)

sheriff = "sheriff"
deputy = "deputy"
outlaw = "outlaw"
renegade = "renegade"

image_sheriff = pygame.image.load(f'image/job/{sheriff}.png')
image_deputy = pygame.image.load(f'image/job/{deputy}.png')
image_outlaw = pygame.image.load(f'image/job/{outlaw}.png')
image_renegade = pygame.image.load(f'image/job/{renegade}.png')


willy_the_kid = "willy_the_kid"
calamity_janet = "calamity_janet"
kit_carlson = "kit_carlson"
bart_cassidy = "bart_cassidy"
sid_ketchum = "sid_ketchum"

image_willy_the_kid = pygame.image.load(f'image/char/{willy_the_kid}.png')
image_calamity_janet = pygame.image.load(f'image/char/{calamity_janet}.png')
image_kit_carlson = pygame.image.load(f'image/char/{kit_carlson}.png')
image_bart_cassidy = pygame.image.load(f'image/char/{bart_cassidy}.png')
image_sid_ketchum = pygame.image.load(f'image/char/{sid_ketchum}.png')


sA_bang = "sA_bang"
c2_bang = "c2_bang"
c3_bang = "c3_bang"
c4_bang = "c4_bang"
c5_bang = "c5_bang"
c6_bang = "c6_bang"
c7_bang = "c7_bang"
c8_bang = "c8_bang"
c9_bang = "c9_bang"
d2_bang = "d2_bang"
d3_bang = "d3_bang"
d4_bang = "d4_bang"
d5_bang = "d5_bang"
d6_bang = "d6_bang"
d7_bang = "d7_bang"
d8_bang = "d8_bang"
d9_bang = "d9_bang"
d10_bang = "d10_bang"
dJ_bang = "dJ_bang"
dQ_bang = "dQ_bang"
dK_bang = "dK_bang"
dA_bang = "dA_bang"
hQ_bang = "hQ_bang"
hK_bang = "hK_bang"
hA_bang = "hA_bang"
s2_missed = "s2_missed"
s3_missed = "s3_missed"
s4_missed = "s4_missed"
s5_missed = "s5_missed"
s6_missed = "s6_missed"
s7_missed = "s7_missed"
s8_missed = "s8_missed"
c10_missed = "c10_missed"
cJ_missed = "cJ_missed"
cQ_missed = "cQ_missed"
cK_missed = "cK_missed"
cA_missed = "cA_missed"

image_sA_bang = pygame.image.load(f'image/item/{sA_bang}.png')
image_c2_bang = pygame.image.load(f'image/item/{c2_bang}.png')
image_c3_bang = pygame.image.load(f'image/item/{c3_bang}.png')
image_c4_bang = pygame.image.load(f'image/item/{c4_bang}.png')
image_c5_bang = pygame.image.load(f'image/item/{c5_bang}.png')
image_c6_bang = pygame.image.load(f'image/item/{c6_bang}.png')
image_c7_bang = pygame.image.load(f'image/item/{c7_bang}.png')
image_c8_bang = pygame.image.load(f'image/item/{c8_bang}.png')
image_c9_bang = pygame.image.load(f'image/item/{c9_bang}.png')
image_d2_bang = pygame.image.load(f'image/item/{d2_bang}.png')
image_d3_bang = pygame.image.load(f'image/item/{d3_bang}.png')
image_d4_bang = pygame.image.load(f'image/item/{d4_bang}.png')
image_d5_bang = pygame.image.load(f'image/item/{d5_bang}.png')
image_d6_bang = pygame.image.load(f'image/item/{d6_bang}.png')
image_d7_bang = pygame.image.load(f'image/item/{d7_bang}.png')
image_d8_bang = pygame.image.load(f'image/item/{d8_bang}.png')
image_d9_bang = pygame.image.load(f'image/item/{d9_bang}.png')
image_d10_bang = pygame.image.load(f'image/item/{d10_bang}.png')
image_dJ_bang = pygame.image.load(f'image/item/{dJ_bang}.png')
image_dQ_bang = pygame.image.load(f'image/item/{dQ_bang}.png')
image_dK_bang = pygame.image.load(f'image/item/{dK_bang}.png')
image_dA_bang = pygame.image.load(f'image/item/{dA_bang}.png')
image_hQ_bang = pygame.image.load(f'image/item/{hQ_bang}.png')
image_hK_bang = pygame.image.load(f'image/item/{hK_bang}.png')
image_hA_bang = pygame.image.load(f'image/item/{hA_bang}.png')
image_s2_missed = pygame.image.load(f'image/item/{s2_missed}.png')
image_s3_missed = pygame.image.load(f'image/item/{s3_missed}.png')
image_s4_missed = pygame.image.load(f'image/item/{s4_missed}.png')
image_s5_missed = pygame.image.load(f'image/item/{s5_missed}.png')
image_s6_missed = pygame.image.load(f'image/item/{s6_missed}.png')
image_s7_missed = pygame.image.load(f'image/item/{s7_missed}.png')
image_s8_missed = pygame.image.load(f'image/item/{s8_missed}.png')
image_c10_missed = pygame.image.load(f'image/item/{c10_missed}.png')
image_cJ_missed = pygame.image.load(f'image/item/{cJ_missed}.png')
image_cQ_missed = pygame.image.load(f'image/item/{cQ_missed}.png')
image_cK_missed = pygame.image.load(f'image/item/{cK_missed}.png')
image_cA_missed = pygame.image.load(f'image/item/{cA_missed}.png')



# 플레이어 수
player_cnt = 2

# 보드
image_boards = []

# 플레이어 카드, 덱, 버려진 덱
players = []
deck = []
abandoned = []

# 직업카드, 캐릭터카드, 오리지널 및 확장
jobs = []
chars = []
chars_original = []
chars_dodgecity = []
chars_wildwestshow = []
chars_thevalleyofshadow = []

# 플레이어 클래스 정의
class Player:
  def __init__(self, image_board):
    # 생명력
    self.image_board = image_board
    self.maxlife = None
    self.life = None

    # 총
    self.gun_range = 1
    self.gun_name = None
    self.bang_cnt = 1

    # 사거리
    self.item_range = 1
    self.add_range_to = 0
    self.sub_range_from = 0

    # 플레이어별 카드
    self.job = None
    self.char = None
    self.gun = None
    self.hand = []
    self.equipped = []

  def set_job(self, job):
    self.job = job
  
  def set_char(self, char):
    self.char = char
    self.maxlife = char.life
    self.life = char.life
    if self.job.name == "sheriff":
      self.maxlife += 1
      self.life += 1

  def set_hand(self, item):
    self.hand.append(item)

# 직업카드 클래스 정의
class Job:
  def __init__(self, filename, image):
    self.name = filename
    self.image = image

# 캐릭터카드 클래스 정의
class Char:
  def __init__(self, filename, image, life=4):
    self.name = filename
    self.image = image
    self.life = life

# 플레잉카드 클래스 정의
class Item:
  def __init__(self, filename, image):
    self.filename = filename
    self.image = image
    self.name = filename.split("_")[1]
    self.suit = filename[0]
    self.rank = filename.split("_")[0][1:]

# 직업 생성
sheriff = Job(sheriff, image_sheriff)
deputy = Job(deputy, image_deputy)
outlaw = Job(outlaw, image_outlaw)
renegade = Job(renegade, image_renegade)

# 보드에 이미지 넣고 섞기
image_boards.extend([image_board0, image_board1, image_board2, image_board3, \
                    image_board4, image_board5, image_board6, image_board7])
# random.shuffle(image_boards) # 테스트 할때는 셔플 막음

# 플레이어 생성 및 직업 추가
player0 = Player(image_boards.pop())
players.append(player0)
jobs.append(outlaw)

if player_cnt >= 2:
  player1 = Player(image_boards.pop())
  player1.image_board = pygame.transform.rotate(player1.image_board, 180)
  players.append(player1)
  jobs.append(renegade)

if player_cnt >= 3:
  player2 = Player(image_boards.pop())
  players.append(player2)
  jobs.append(deputy)

if player_cnt >= 4:
  player3 = Player(image_boards.pop())
  players.append(player3)
  jobs.remove(deputy)
  jobs.append(outlaw)
  jobs.append(sheriff)

if player_cnt >= 5:
  player4 = Player(image_boards.pop())
  players.append(player4)
  jobs.append(deputy)

if player_cnt >= 6:
  player5 = Player(image_boards.pop())
  players.append(player5)
  jobs.append(outlaw)

if player_cnt >= 7:
  player6 = Player(image_boards.pop())
  players.append(player6)
  jobs.append(deputy)

if player_cnt >= 8:
  player7 = Player(image_boards.pop())
  players.append(player7)
  jobs.append(renegade)

# 직업 섞기
random.shuffle(jobs)
# 직업 이름 출력
# print([jobs[i].name for i in range(5)], sep=' ')

# 캐릭터 섞기 위해 리스트에 추가
chars_original.append(Char(willy_the_kid, image_willy_the_kid))
chars_original.append(Char(calamity_janet, image_calamity_janet))
chars_original.append(Char(kit_carlson, image_kit_carlson))
chars_original.append(Char(bart_cassidy, image_bart_cassidy))
chars_original.append(Char(sid_ketchum, image_sid_ketchum))

# 어느 버전 캐릭터까지 사용할지 선택
chars = chars_original #\
      # + chars_dodgecity \
      # + chars_wildwestshow \
      # + chars_thevalleyofshadow

# 캐릭터 섞기
random.shuffle(chars)

# 플레이어별 직업 및 캐릭터 할당
for i in range(player_cnt):
  players[i].set_job(jobs[i])
  players[i].set_char(chars[i])
  # print(f'player{i}.job: {players[i].job.name}, player{i}.char: {players[i].char.name}')

# 플레잉카드 생성
deck.append(Item(sA_bang, image_sA_bang))
deck.append(Item(c2_bang, image_c2_bang))
deck.append(Item(c3_bang, image_c3_bang))
deck.append(Item(c4_bang, image_c4_bang))
deck.append(Item(c5_bang, image_c5_bang))
deck.append(Item(c6_bang, image_c6_bang))
deck.append(Item(c7_bang, image_c7_bang))
deck.append(Item(c8_bang, image_c8_bang))
deck.append(Item(c9_bang, image_c9_bang))
deck.append(Item(d2_bang, image_d2_bang))
deck.append(Item(d3_bang, image_d3_bang))
deck.append(Item(d4_bang, image_d4_bang))
deck.append(Item(d5_bang, image_d5_bang))
deck.append(Item(d6_bang, image_d6_bang))
deck.append(Item(d7_bang, image_d7_bang))
deck.append(Item(d8_bang, image_d8_bang))
deck.append(Item(d9_bang, image_d9_bang))
deck.append(Item(d10_bang, image_d10_bang))
deck.append(Item(dJ_bang, image_dJ_bang))
deck.append(Item(dQ_bang, image_dQ_bang))
deck.append(Item(dK_bang, image_dK_bang))
deck.append(Item(dA_bang, image_dA_bang))
deck.append(Item(hQ_bang, image_hQ_bang))
deck.append(Item(hK_bang, image_hK_bang))
deck.append(Item(hA_bang, image_hA_bang))
deck.append(Item(s2_missed, image_s2_missed))
deck.append(Item(s3_missed, image_s3_missed))
deck.append(Item(s4_missed, image_s4_missed))
deck.append(Item(s5_missed, image_s5_missed))
deck.append(Item(s6_missed, image_s6_missed))
deck.append(Item(s7_missed, image_s7_missed))
deck.append(Item(s8_missed, image_s8_missed))
deck.append(Item(c10_missed, image_c10_missed))
deck.append(Item(cJ_missed, image_cJ_missed))
deck.append(Item(cQ_missed, image_cQ_missed))
deck.append(Item(cK_missed, image_cK_missed))
deck.append(Item(cA_missed, image_cA_missed))

# 플레잉카드 섞기
random.shuffle(deck)
# for i in range(4):
  # print(f'{deck[i].name} {deck[i].rank}{deck[i].suit}')

# 플레잉카드 생명력 만큼 나눠주기
for i in range(player_cnt):
  get_cnt = players[i].life

  for j in range(get_cnt):
    players[i].set_hand(deck.pop())

# 손패 확인
# for i in range(player_cnt):
#   print(f'player{i}: ', end=" ")
#   for j in range(len(players[i].hand)):
#     print(players[i].hand.pop().filename, end="  ")
#   print()

print(player0.job.name)

play = True
while play:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      print(pygame.mouse.get_pos())

  screen.fill((0,0,0))
  
  if player_cnt == 2:
    # 보드판 그리기
    screen.blit(player0.image_board, ((size_bg_w - image_size_ws[0]) / 2, size_bg_h - image_size_hs[0]))
    screen.blit(player1.image_board, ((size_bg_w - image_size_ws[1]) / 2, 0))

    # 총알 그리기
    for i in range(player_cnt):

      bullet_start_pos_xs = []
      bullet_start_pos_ys = []
      bullet_gap = 0

      bullet_start_pos_xs.extend([580, 930])
      bullet_start_pos_ys.extend([595, 225])

      # 남은 생명력
      for j in range(players[i].life):

        # player별
        if i == 0:
          screen.blit(image_bullet_front_down, (bullet_start_pos_xs[i] + bullet_gap, bullet_start_pos_ys[i]))
        elif i == 1:
          screen.blit(image_bullet_front_up, (bullet_start_pos_xs[i] - bullet_gap, bullet_start_pos_ys[i]))

        bullet_gap += 85

      # 잃은 생명력
      losslife = players[i].maxlife - players[i].life
      for j in range(losslife):

        # player별
        if i == 0:
          screen.blit(image_bullet_back_down, (bullet_start_pos_xs[i] + bullet_gap, bullet_start_pos_ys[i]))
        elif i == 1:
          screen.blit(image_bullet_back_up, (bullet_start_pos_xs[i] - bullet_gap, bullet_start_pos_ys[i]))


  pygame.display.update()

pygame.quit()