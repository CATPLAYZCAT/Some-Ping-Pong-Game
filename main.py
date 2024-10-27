from pygame import *
from random import randint

window = display.set_mode((700,500))
window_width = 700
window_height = 500

speed_x = 3
speed_y = 3

isGamerunning = True
clock = time.Clock()
FPS = 60

display.set_caption("Ping Pong")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_x_size, player_y_size):
      super().__init__()

      self.image = transform.scale(image.load(player_image),(player_x_size,player_y_size))
      self.speed = player_speed

      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed


class Enemy(GameSprite):
   def update(self):
       self.rect.x += self.speed
       global miss
       if self.rect.x > window_height:
           self.rect.y  = randint(0, window_height - 80)
           self.rect.x = 0

Left_Player = Player("rocket.png", 0,50,15,80,300)
Right_Player = Player("rocket.png", 620,50,15,80,300)
Ball = Enemy("ufo.png",0,0,0,125,100)


while isGamerunning:
    window.blit(transform.scale(image.load("galaxy.jpg"), (700,500)), (0,0))
    Left_Player.reset()
    Right_Player.reset()
    Ball.reset()
    Left_Player.update_L()
    Right_Player.update_R()
    Ball.update()

    #if sprite.collide_rect(Left_Player, Ball) or sprite.collide_rect(Right_Player,Ball):


    display.update()
    clock.tick(FPS)
    for e in event.get():
        keys = key.get_pressed()
        if e.type == QUIT:
            isGamerunning = False
