import pygame
import random
# from job import Job, sheriff, outlaw, deputy, renegade

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("BANG!")

image_board0 = pygame.image.load("image/board/board0.png")
image_board1 = pygame.image.load("image/board/board1.png")
image_board2 = pygame.image.load("image/board/board2.png")
image_board3 = pygame.image.load("image/board/board3.png")
image_board4 = pygame.image.load("image/board/board4.png")
image_board5 = pygame.image.load("image/board/board5.png")
image_board6 = pygame.image.load("image/board/board6.png")
image_board7 = pygame.image.load("image/board/board7.png")

image_bullet_front = pygame.image.load("image/bullet/bullet_front.png")
image_bullet_back = pygame.image.load("image/bullet/bullet_back.png")

image_sheriff = pygame.image.load("image/job/sheriff.png")
image_deputy = pygame.image.load("image/job/deputy.png")
image_outlaw = pygame.image.load("image/job/outlaw.png")
image_renegade = pygame.image.load("image/job/renegade.png")

image_willy_the_kid = pygame.image.load("image/char/willy_the_kid.png")
image_calamity_janet = pygame.image.load("image/char/calamity_janet.png")
image_kit_carlson = pygame.image.load("image/char/kit_carlson.png")
image_bart_cassidy = pygame.image.load("image/char/bart_cassidy.png")
image_sid_ketchum = pygame.image.load("image/char/sid_ketchum.png")

sA_bang = "sA_bang.png"
c2_bang = "c2_bang.png"
c3_bang = "c3_bang.png"
c4_bang = "c4_bang.png"
c5_bang = "c5_bang.png"
c6_bang = "c6_bang.png"
c7_bang = "c7_bang.png"
c8_bang = "c8_bang.png"
c9_bang = "c9_bang.png"
d2_bang = "d2_bang.png"
d3_bang = "d3_bang.png"
d4_bang = "d4_bang.png"
d5_bang = "d5_bang.png"
d6_bang = "d6_bang.png"
d7_bang = "d7_bang.png"
d8_bang = "d8_bang.png"
d9_bang = "d9_bang.png"
d10_bang = "d10_bang.png"
dJ_bang = "dJ_bang.png"
dQ_bang = "dQ_bang.png"
dK_bang = "dK_bang.png"
dA_bang = "dA_bang.png"
hQ_bang = "hQ_bang.png"
hK_bang = "hK_bang.png"
hA_bang = "hA_bang.png"
s2_missed = "s2_missed.png"
s3_missed = "s3_missed.png"
s4_missed = "s4_missed.png"
s5_missed = "s5_missed.png"
s6_missed = "s6_missed.png"
s7_missed = "s7_missed.png"
s8_missed = "s8_missed.png"
c10_missed = "c10_missed.png"
cJ_missed = "cJ_missed.png"
cQ_missed = "cQ_missed.png"
cK_missed = "cK_missed.png"
cA_missed = "cA_missed.png"

# 플레이어 수
player_cnt = 2

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
  def __init__(self):
    # 생명력
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
    self.life = char.life
    if self.job.name == "Sheriff":
      self.life += 1

  def get_hand(self, item):
    self.hand.append(item)

# 직업카드 클래스 정의
class Job:
  def __init__(self, name, image):
    self.name = name
    self.image = image

# 캐릭터카드 클래스 정의
class Char:
  def __init__(self, name, image, life=4):
    self.name = name
    self.image = image
    self.life = life
    self.image = None

# 플레잉카드 클래스 정의
class Item:
  def __init__(self, filename):
    self.filename = filename
    self.name = filename.split("_")[1].split(".")[0].upper()
    self.image = pygame.image.load(f'image/item/{filename}')
    self.suit = filename[0]
    self.rank = filename.split("_")[0][1:]

# 직업 생성
sheriff = Job("Sheriff", image_sheriff)
outlaw = Job("Outlaw", image_outlaw)
deputy = Job("Deputy", image_deputy)
renegade = Job("Renegade", image_renegade)

# 플레이어 생성 및 직업 추가
player0 = Player()
players.append(player0)
jobs.append(outlaw)

if player_cnt >= 2:
  player1 = Player()
  players.append(player1)
  jobs.append(renegade)

if player_cnt >= 3:
  player2 = Player()
  players.append(player2)
  jobs.append(deputy)

if player_cnt >= 4:
  player3 = Player()
  players.append(player3)
  jobs.remove(deputy)
  jobs.append(outlaw)
  jobs.append(sheriff)

if player_cnt >= 5:
  player4 = Player()
  players.append(player4)
  jobs.append(deputy)

if player_cnt >= 6:
  player5 = Player()
  players.append(player5)
  jobs.append(outlaw)

if player_cnt >= 7:
  player6 = Player()
  players.append(player6)
  jobs.append(deputy)

if player_cnt >= 8:
  player7 = Player()
  players.append(player7)
  jobs.append(renegade)

# 직업 섞기
random.shuffle(jobs)
# 직업 이름 출력
# print([jobs[i].name for i in range(5)], sep=' ')

# 캐릭터 생성
# willy_the_kid = Char("WILLY THE KID")
# calamity_janet = Char("CALAMITY JANET")
# kit_carlson = Char("KIT CARLSON")
# bart_cassidy = Char("BART CASSIDY")
# sid_ketchum = Char("SID KETCHUM")

# 캐릭터 섞기 위해 리스트에 추가
chars_original.append(Char("WILLY THE KID", image_willy_the_kid))
chars_original.append(Char("CALAMITY JANET", image_calamity_janet))
chars_original.append(Char("KIT CARLSON", image_kit_carlson))
chars_original.append(Char("BART CASSIDY", image_bart_cassidy))
chars_original.append(Char("SID KETCHUM", image_sid_ketchum))

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
deck.append(Item(sA_bang))
deck.append(Item(c2_bang))
deck.append(Item(c3_bang))
deck.append(Item(c4_bang))
deck.append(Item(c5_bang))
deck.append(Item(c6_bang))
deck.append(Item(c7_bang))
deck.append(Item(c8_bang))
deck.append(Item(c9_bang))
deck.append(Item(d2_bang))
deck.append(Item(d3_bang))
deck.append(Item(d4_bang))
deck.append(Item(d5_bang))
deck.append(Item(d6_bang))
deck.append(Item(d7_bang))
deck.append(Item(d8_bang))
deck.append(Item(d9_bang))
deck.append(Item(d10_bang))
deck.append(Item(dJ_bang))
deck.append(Item(dQ_bang))
deck.append(Item(dK_bang))
deck.append(Item(dA_bang))
deck.append(Item(hQ_bang))
deck.append(Item(hK_bang))
deck.append(Item(hA_bang))

deck.append(Item(s2_missed))
deck.append(Item(s3_missed))
deck.append(Item(s4_missed))
deck.append(Item(s5_missed))
deck.append(Item(s6_missed))
deck.append(Item(s7_missed))
deck.append(Item(s8_missed))
deck.append(Item(c10_missed))
deck.append(Item(cJ_missed))
deck.append(Item(cQ_missed))
deck.append(Item(cK_missed))
deck.append(Item(cA_missed))

# 플레잉카드 섞기
random.shuffle(deck)
# for i in range(4):
  # print(f'{deck[i].name} {deck[i].rank}{deck[i].suit}')

# 플레잉카드 생명력 만큼 나눠주기
for i in range(player_cnt):
  get_cnt = players[i].life

  for j in range(get_cnt):
    players[i].get_hand(deck.pop())

play = True
while play:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

  screen.fill((0,0,0))

  pygame.display.update()

pygame.quit()