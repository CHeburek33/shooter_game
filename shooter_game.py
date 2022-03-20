from pygame import *
from random import randint
from time import sleep
lostenemy = 0
killingenemy = 0
zad_bullet = 0
zad_max_bullet = 15
money = 15
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,scale_x,scale_y):
        super().__init__()
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = transform.scale(image.load(player_image), (self.scale_x, self.scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,scale_x,scale_y,health):
        self.health = health
        super().__init__(player_image, player_x, player_y, player_speed,scale_x,scale_y)

    def shot(self):
        if self.health > 0:
            keys_pressed = key.get_pressed()
            global zad_bullet
            if zad_bullet == zad_max_bullet :
                if keys_pressed[K_SPACE]:
                    bullet =  Bullet('bullet.png',player.rect.x + 18,player.rect.y -10,6,20,40)
                    bullets.add(bullet)
                    fire.play()
                    zad_bullet = 0
            else:
                zad_bullet +=1
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]and self.rect.x >5:
            self.rect.x -= self.speed
        if keys_pressed[K_d]and self.rect.x <win_x-self.scale_y:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.y <= win_y+100:
            self.rect.y += self.speed
        if self.rect.y >= 800:
            global lostenemy
            self.rect.y = -20
            self.rect.x = randint(100,win_x-100)
            lostenemy += 1
class Bullet(GameSprite):
    def update(self):
        if self.rect.y != -150:
            self.rect.y -= self.speed
        if self.rect.y <= -20:
            self.kill()
class Menu():
    def __init__(self,punkt,spriteMenu1,spriteMenu2,x,y,scalex,scaley,index):
        self.punkt = punkt
        self.scalex = scalex
        self.scaley = scaley
        self.image = [transform.scale(image.load(spriteMenu1), (self.scalex, self.scaley)),transform.scale(image.load(spriteMenu2), (self.scalex, self.scaley))]
        self.index = index
        self.x = x 
        self.y = y
    def reset(self):
        window.blit(self.image[self.index],(self.x,self.y))
    def button_pressed(self):
        global menu, game
        x_mouse, y_mouse = mouse.get_pos()
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN:
                if i.button == 1:
                    if x_mouse >= self.x and x_mouse <= self.x + self.scalex and y_mouse >= self.y and y_mouse <= self.y + self.scaley:
                        menu = False 
                        game = True
        if x_mouse >= self.x and x_mouse <= self.x + self.scalex and y_mouse >= self.y and y_mouse <= self.y + self.scaley:
            self.index = 1
        else:
            self.index = 0
class Upgrade_Menu():
    def __init__(self,punkt,sprite_upgrade1,sprite_updrade2,x,y,scalex,scaley,index):
        self.punkt = punkt
        self.scalex = scalex
        self.scaley = scaley
        self.image = [transform.scale(image.load(sprite_upgrade1), (self.scalex, self.scaley)),transform.scale(image.load(sprite_updrade2), (self.scalex, self.scaley))]
        self.index = index
        self.x = x 
        self.y = y
    def reset(self):
        window.blit(self.image[self.index],(self.x,self.y))
    def button_pressed(self):
        global menu, game, upgrademenu
        x_mouse, y_mouse = mouse.get_pos()
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN:
                if i.button == 1:
                    if x_mouse >= self.x and x_mouse <= self.x + self.scalex and y_mouse >= self.y and y_mouse <= self.y + self.scaley:
                        menu = False 
                        game = False
                        upgrademenu = True
        if x_mouse >= self.x and x_mouse <= self.x + self.scalex and y_mouse >= self.y and y_mouse <= self.y + self.scaley:
            self.index = 1
        else:
            self.index = 0
class Button_Exit():
    def __init__(self,punkt,sprite_upgrade1,sprite_updrade2,x,y,scalex,scaley,index):
        self.punkt = punkt
        self.scalex = scalex
        self.scaley = scaley
        self.image = [transform.scale(image.load(sprite_upgrade1), (self.scalex, self.scaley)),transform.scale(image.load(sprite_updrade2), (self.scalex, self.scaley))]
        self.index = index
        self.x = x 
        self.y = y
    def reset(self):
        window.blit(self.image[self.index],(self.x,self.y))

win_x = 900
win_y = 700
window = display.set_mode((win_x, win_y))
display.set_caption("Maze")

#Surface
surf1 = Surface((win_x,win_y))
surf1.fill((188, 120, 145))

surf2 = Surface((win_x,win_y)) 
surf2.fill((101, 157, 187))

player = Player('rocket.png',80,625,7,65,85,3)
galaxy = GameSprite('galaxy.jpg',0,0,0,win_x,win_y)
Button_Play = Menu('Game','Play1.png','Play2.png',250,100,400,200,0)
Button_Upgrade = Upgrade_Menu('Upgrade','Upgrade1.png','Upgrade2.png',250,400,400,200,0)
ButtonExit = Upgrade_Menu('Exit','exit1.png','exit2.png',10,10,35,35,0)
bullets = sprite.Group()
monsters = sprite.Group()
#enemy = Enemy('ufo.png',randint(100,win_x-100),-20,randint(2,6),65,65)
for i in range(5):
    enemy = Enemy('ufo.png',randint(100,win_x-100),-20,randint(2,6),65,65)
    monsters.add(enemy)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')

font.init()
font = font.Font(None,25)

run = True
#Меню и игра
game = False
menu = True
upgrademenu = False
clock = time.Clock()
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not(game) and not(menu) and upgrademenu:
        #Upgrade
        window.blit(surf2,(0,0)) 


        ButtonExit.reset()

        display.update()
    elif not(game) and menu and not(upgrademenu):
        #Отрисовка surface
        window.blit(surf1,(0,0)) 
        
        Button_Play.reset()
        Button_Upgrade.reset()

        Button_Play.button_pressed()
        Button_Upgrade.button_pressed()
        display.update()

    elif game and not(menu) and not(upgrademenu):

        if sprite.groupcollide(monsters,bullets,True,True):
            killingenemy += 1
            enemy = Enemy('ufo.png',randint(100,win_x-100),-20,randint(2,6),65,65)
            monsters.add(enemy)
            money += 3
        if sprite.spritecollide(player,monsters,True):
            player.health -= 1
            enemy = Enemy('ufo.png',randint(100,win_x-100),-20,randint(2,6),65,65)
            monsters.add(enemy)
            if player.health<=0:
                game = False
                menu = True
                upgrademenu = False
                player.health = 3
                for i in monsters:
                    i.kill()
                for i in bullets:
                    i.kill()
                time.delay(3000)
                for i in range(5):
                    enemy = Enemy('ufo.png',randint(100,win_x-100),-20,randint(2,6),65,65)
                    monsters.add(enemy)
                

        keys_pressed = key.get_pressed()
        if keys_pressed[K_ESCAPE] and game == True and menu == False:
            game = False
            menu = True

        galaxy.reset()
        player.update()
        monsters.update()
        monsters.draw(window)
        
        bullets.update()
        bullets.draw(window)
        win = font.render(
            'Убитых кораблей '+str(killingenemy),True,(255,0,0)
        )
        lose = font.render(
            'Пропущенных кораблей '+str(lostenemy),True,(124,215,0)
        )
        moneycol = font.render(
            'Монеты '+str(money),True,(255, 255, 0)
        )

        window.blit(win,(10,10))
        window.blit(lose,(10,25))
        window.blit(moneycol,(10,40))

        player.shot()
        player.reset()

        display.update()
        clock.tick(FPS)