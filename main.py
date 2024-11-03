from pygame import *
from random import randint

window = display.set_mode((700,500))
window_width = 700
window_height = 500



speed_x = 5
speed_y = 5

isGamerunning = True
isFinish = False
isCollided = False
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
        if keys[K_DOWN] and self.rect.y < 280:
            self.rect.y += self.speed

    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 280:
            self.rect.y += self.speed


class Enemy(GameSprite):
   def update(self):
       self.rect.x += self.speed

Left_Player = Player("rocket.png", 0,50,10,60,220)
Right_Player = Player("rocket.png", 620,50,10,60,220)
Ball = Enemy("ufo.png",350,250,0,100,75)


while isGamerunning:
    window.blit(transform.scale(image.load("galaxy.jpg"), (700,500)), (0,0))
    Left_Player.reset()
    Right_Player.reset()
    Left_Player.update_L()
    Right_Player.update_R()
  

    if isFinish != True:
        Ball.reset()
        Ball.update()
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y

    if sprite.collide_rect(Left_Player, Ball) or sprite.collide_rect(Right_Player,Ball):
        rng = randint(1,2)
        if isCollided == False:
            isCollided = True
            speed_x *= -1
            speed_y *= -1
            isCollided = False

    if Ball.rect.y > 400 or Ball.rect.y < 0:
        speed_y *= -1
        
    if Ball.rect.x < 0:
        isFinish = True
        isGamerunning = False
        print("P1 LOSE!")
    
    if Ball.rect.x > 700:
        isFinish = True
        isGamerunning = False
        print("P2 LOSE!")

    display.update()
    clock.tick(FPS)
    for e in event.get():
        keys = key.get_pressed()
        if e.type == QUIT:
            isGamerunning = False
