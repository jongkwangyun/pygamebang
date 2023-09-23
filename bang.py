import pygame
import random
# from job import Job, sheriff, outlaw, deputy, renegade

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("BANG!")

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
  def __init__(self, name):
    self.name = name

# 캐릭터카드 클래스 정의
class Char:
  def __init__(self, name, life=4):
    self.name = name
    self.life = life

# 플레잉카드 클래스 정의
class Item:
  def __init__(self, name, rank, suit):
    self.name = name
    self.rank = rank
    self.suit = suit

# 직업 생성
sheriff = Job("Sheriff")
outlaw = Job("Outlaw")
deputy = Job("Deputy")
renegade = Job("Renegade")

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
# print([jobs[i].name for i in range(5)], sep=' ')

# 캐릭터 생성
# willy_the_kid = Char("WILLY THE KID")
# calamity_janet = Char("CALAMITY JANET")
# kit_carlson = Char("KIT CARLSON")
# bart_cassidy = Char("BART CASSIDY")
# sid_ketchum = Char("SID KETCHUM")

# 캐릭터 섞기 위해 리스트에 추가
chars_original.append(Char("WILLY THE KID"))
chars_original.append(Char("CALAMITY JANET"))
chars_original.append(Char("KIT CARLSON"))
chars_original.append(Char("BART CASSIDY"))
chars_original.append(Char("SID KETCHUM"))

# 어느 버전 캐릭터까지 사용할지 선택
chars = chars_original \
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
deck.append(Item("BANG!", "Q", "heart"))
deck.append(Item("BANG!", "K", "heart"))
deck.append(Item("BANG!", "A", "heart"))
deck.append(Item("BANG!", "2", "diamond"))
deck.append(Item("BANG!", "3", "diamond"))
deck.append(Item("BANG!", "4", "diamond"))
deck.append(Item("BANG!", "5", "diamond"))
deck.append(Item("BANG!", "6", "diamond"))
deck.append(Item("BANG!", "7", "diamond"))
deck.append(Item("BANG!", "8", "diamond"))
deck.append(Item("BANG!", "9", "diamond"))
deck.append(Item("BANG!", "10", "diamond"))
deck.append(Item("BANG!", "J", "diamond"))
deck.append(Item("BANG!", "Q", "diamond"))
deck.append(Item("BANG!", "K", "diamond"))
deck.append(Item("BANG!", "A", "diamond"))
deck.append(Item("BANG!", "2", "club"))
deck.append(Item("BANG!", "3", "club"))
deck.append(Item("BANG!", "4", "club"))
deck.append(Item("BANG!", "5", "club"))
deck.append(Item("BANG!", "6", "club"))
deck.append(Item("BANG!", "7", "club"))
deck.append(Item("BANG!", "8", "club"))
deck.append(Item("BANG!", "9", "club"))
deck.append(Item("BANG!", "A", "spade"))

deck.append(Item("MISSED!", "2", "spade"))
deck.append(Item("MISSED!", "3", "spade"))
deck.append(Item("MISSED!", "4", "spade"))
deck.append(Item("MISSED!", "5", "spade"))
deck.append(Item("MISSED!", "6", "spade"))
deck.append(Item("MISSED!", "7", "spade"))
deck.append(Item("MISSED!", "8", "spade"))
deck.append(Item("MISSED!", "10", "club"))
deck.append(Item("MISSED!", "J", "club"))
deck.append(Item("MISSED!", "Q", "club"))
deck.append(Item("MISSED!", "K", "club"))
deck.append(Item("MISSED!", "A", "club"))


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