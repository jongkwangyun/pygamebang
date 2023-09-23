import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("BANG!")

players = []
deck = []
abandoned = []


class Job:
  def __init__(self, name, name_kor):
    self.name = name
    self.name_kor = name_kor

class Player:
  def __init__(self):
    self.life = None

    self.gun_range = 1
    self.gun_name = None
    self.bang_cnt = 1

    self.item_range = 1
    self.add_range_to = 0
    self.sub_range_from = 0

    self.job = None
    self.charac = None
    self.hand = []
    self.gun = []
    self.equipped = []

  def set_job(self, job):
    self.job = job

class Charac:
  def __init__(self):
    self.name = None
    self.name_kor = None
    self.life = 4
    
class Item:
  def __init__(self):
    self.name = None
    self.name_kor = None
    self.rank = None
    self.suit = None

player0 = Player()
sheriff = Job("Sheriff", "보안관")
player0.set_job(sheriff)


print(player0.job.name)
print(player0.job.name_kor)


play = True
while play:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

  screen.fill((0,0,0))

  pygame.display.update()

pygame.quit()