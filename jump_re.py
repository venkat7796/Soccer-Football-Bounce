import pygame
pygame.init()

#Creating a window
win = pygame.display.set_mode((480,360))
#Caption for our window
pygame.display.set_caption("A new atmosphere")

#Assign the background image to a variable
bg = pygame.image.load('cart2.jpg')
#Assign the football image to a variable
ba = pygame.image.load('fb5.png')
#Assign the obstacle image to a variable
ob = pygame.image.load('co_7.png')
bb = pygame.image.load('ucl large1.jpg')
#Add music to our game
pl = pygame.mixer.music.load('pl2.mp3')
pygame.mixer.music.play(-1)
#Adding a sound effect for kick
kk = pygame.mixer.Sound('kick.wav')
#Adding a sound effect for collision
ref = pygame.mixer.Sound('ref.wav')
class football(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.isjump = False
        self.jump = 10
        self.hitbox = (x,y,64,58)
        self.visible = True

    def draw_ball(self,win):
        win.blit(ba,(self.x,self.y))
        self.hitbox = (self.x + 5,self.y,53,58)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
    
    def hit(self):
        print("Hit")
        ref.play()
        
class enemy(object):
    def __init__(self,x,y,w,h,end):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.path = [x,end]
        self.vel = 7
        self.hitbox = (x,y,40,138)

    def create_enemy(self,win):
        self.move_enemy()
        win.blit(ob,(self.x,self.y))
        self.hitbox = (self.x + 40,self.y,40,138)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def move_enemy(self):
        #if self.vel > 0:
            #if self.x < self.path[1] - self.w:
                #self.x = self.x + self.vel
            #else:
                #self.vel = self.vel * -1
        #else:
            #if self.x > self.path[0] - 35:
                #self.x = self.x + self.vel
            #else:
                #self.vel = self.vel * -1
        if self.x > self.path[1] - self.w:
            self.x = -15
        elif self.x < self.path[0] - 35:
            self.x = self.path[1]
        else:
            self.x = self.x + self.vel
        
        
#Function to display the image in our window
def draw_out(win,score):
    #bg is the variable that contains our image
    #(0,0) is the x and y co-ordinates in our 2D system
    #This means that image will originate from the origin which
    #is top left point in our window
    win.blit(bg,(0,0))
    #Now displaying it in our screen
    #text = fo.render('Score : ' + str(score),1,(0,0,0))
    #win.blit(text,(150,50))
    #Calling football class via instance ball
    if ball.visible:
        text = fo.render('Score : ' + str(score),1,(0,0,0))
        win.blit(text,(150,50))
        ball.draw_ball(win)
        #Calling enemy class via instance po
        po.create_enemy(win)
        if ball.y > po.hitbox[1] and ball.y < po.hitbox[1] + po.hitbox[3]:
            if ball.x > po.hitbox[0] and ball.x < po.hitbox[0] + po.hitbox[2]:
                ball.hit()
                ball.visible = False
    else:
        #win.blit(bb,(100,50))
        tbs = bs.render('Your Score : ' + str(score),1,(0,0,0))
        win.blit(tbs,(125,200))
    pygame.display.update()
#variable that will keep the execution 
run = True
ball = football(200,300,64,64)
po = enemy(10,220,120,142,500)
fo = pygame.font.SysFont('comicsans',50,True,True)
bs = pygame.font.SysFont('Segoe UI', 35,False,True)
#Create a new variable named score
score = 0
time = 0
while run:
    #getting the events
    pygame.time.delay(25)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            #reversing the variable to terminate the execution
            run = False
    keys = pygame.key.get_pressed()
    if ball.visible:
        time = time + 1
        if time % 5 == 0:
            score = score + 1
    if not(ball.isjump):
        if keys[pygame.K_SPACE]:
            kk.play()
            ball.isjump = True
    else:
        if ball.jump >= -10:
            fig = 1
            if ball.jump < 0:
                fig = -1
            ball.y = ball.y - (ball.jump ** 2) * 0.5 * fig
            ball.jump = ball.jump - 1
        else:
            ball.isjump = False
            ball.jump = 10
    draw_out(win,score)
pygame.quit()
