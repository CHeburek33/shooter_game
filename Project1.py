from pygame import*

class Card(sprite.Sprite):
    def __init__(self,x, y, width, height,color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
        self.speed_x = 0
        self.speed_y = 0
    def draw(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        draw.rect(window,self.fill_color, self.rect)

class Picture(sprite.Sprite):
    def __init__(self,x, y, width , height, image_name):
        self.rect = Rect(x, y, width, height)
        self.image = image.load(image_name)
        self.image = transform.scale(self.image, (width, height))
        self.imageR = transform.flip(self.image, True, False)
        self.lookingRight = True
        self.speed_x = 0
        self.speed_y = 0

    def draw(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        for i in EnemyList:
            if sprite.collide_rect(Player, i):
                global run
                run = False
                global end 
                end = False
        for i in walls:
            if sprite.collide_rect(Player, i):
                self.rect.x -= self.speed_x
                self.rect.y -= self.speed_y
        
        for i in EndPhoto:
            if sprite.collide_rect(Player, i):
                run = False
                end = True
        if self.lookingRight:
            window.blit(self.image, (self.rect.x, self.rect.y))
        else:
            window.blit(self.imageR, (self.rect.x, self.rect.y))

window = display.set_mode((1000,700))
display.set_caption("PygameMaze")
Background = Picture(0,0, 1000,700, "fields.png")
BlackColor = (0,0,0)
CheckColor = (100,100,100)
wall1 = Card(0, 0, 50000, 20, BlackColor)
wall2 = Card(0,75, 400, 20, BlackColor)
wall3 = Card(475, 75, 440, 20, BlackColor)
wall4 = Card(980, 0, 20, 300, BlackColor )
wall5 = Card(400,75, 20, 200, BlackColor)
wall6 = Card(900,75, 20, 245, BlackColor)
wall7 = Card(915, 300, 100, 20, BlackColor)
wall8 = Card(475,75, 20, 200, BlackColor)
wall9 = Card(475,275,250, 20, BlackColor)
wall10 = Card(725,275, 20, 95, BlackColor)
wall11 = Card(0, 350, 725, 20, BlackColor)
wall12 = Card(0,275, 420, 20, BlackColor )
Purple = Picture(0,295, 30,55, "Purple.png")
walls = [wall1, wall2, wall3,wall4, wall5, wall6, wall7,wall8,wall9,wall10, wall11,wall12]
Lose = Picture(0,0, 1000,700, "Lose.png")
Win = Picture(0,0, 1000,700, "Win.jpg")
Player = Picture(10, 20, 40, 50, "Monkey.png")
Enemy1 = Picture(910,200, 75,100, "GreenDragon.png")
Enemy2 = Picture(670,275, 60,85, "RedDragon.png")
EnemyList = [Enemy1, Enemy2]
EndPhoto = [Purple]
clock = time.Clock()
run = True
end = None

while run:
    clock.tick(30)
    Background.draw()
    Player.draw()
    Purple.draw()
    
    for i in EnemyList:
        i.draw()

    for i in walls:
        i.draw()

    for i in EndPhoto:
        i.draw()

    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_d:
                Player.speed_x = 5
                Player.lookingRight = True
            elif e.key == K_a:
                Player.speed_x = -5
                Player.lookingRight = False
            elif e.key == K_s:
                Player.speed_y = 5
            else:
                if e.key == K_w:
                    Player.speed_y = -5
        if e.type == KEYUP:
            if e.key == K_d:
                Player.speed_x = 0
            elif e.key == K_a:
                Player.speed_x = 0
            elif e.key == K_s:
                Player.speed_y = 0
            else:
                if e.key == K_w:
                    Player.speed_y = 0
        if e.type == QUIT:
            run = False
    display.update()
if end == False:
    while run == False:
        clock.tick(60)
        window.fill((255,255,255))
        Lose.draw()
        for e in event.get():
            if e.type == QUIT:
                run = True
        display.update()
if end == True:
    while run == False:
        clock.tick(60)
        window.fill((255,255,255))
        Win.draw()
        for e in event.get():
            if e.type == QUIT:
                run = True
        display.update()