#SPACE INVADERS;game development with pygame
#importying necessary modules
import pygame,sys
import random
import pygame.locals
from os import path
from pygame import mixer
#pre assignment of values
img_dir=path.join(path.dirname(__file__),'img')
snd_dir=path.join(path.dirname(__file__),'snd')

x=4
y=0
pxchange=0
gameove=False
ly=[1,-1]
#initializing the pygame module
pygame.init()
#clock rate
clock=pygame.time.Clock()
#screen 
screen=pygame.display.set_mode((600,800))
#caption
pygame.display.set_caption("Space Invaders")
#background image
bg=pygame.image.load(path.join(img_dir,"seam3.png"))
bg2=pygame.image.load(path.join(img_dir,"start2.png"))
bg3=pygame.image.load(path.join(img_dir,"rec2.png"))
#game icon
icon=pygame.image.load(path.join(img_dir,"enemy2.png"))
pygame.display.set_icon(icon)

run=True                        #loop for stat screen
while run:
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                 run=False
            if event.key==pygame.K_h:
                while running:          #loop for help screen
                    screen.blit(bg,(0,0))
                    screen.blit(bg3,(0,0))
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_s:
                                run=False
                                running=False
                            if event.key==pygame.K_ESCAPE:
                                running=False
                        elif event.type==pygame.QUIT:
                             pygame.quit()
                             sys.exit()
                    pygame.display.update()
                
        elif event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        running=True    
    pygame.display.update()

#set up assests

file2=open(path.join(img_dir,"game.txt"),"r")             #opening a file
s=int(file2.read())                    #getting the high score
file2.close()                          #closing file

explosion_anim={}                      #preparing sprite sheet
explosion_anim['lg']=[]                #by loading images
explosion_anim['xlg']=[]               #one by one
for i in range(9): 
    filename='tile00{}.png'.format(i)
    img=pygame.image.load(path.join(img_dir,filename))
    img1=pygame.transform.scale(img,(100,100))
    img2=pygame.transform.scale(img,(170,170))
    explosion_anim['lg'].append(img1) 
    explosion_anim['xlg'].append(img2)   
#backgroung music    
mixer.music.load(path.join(snd_dir,"drama.mp3"))          #
mixer.music.play(-1)
bs=mixer.Sound(path.join(snd_dir,"laser.wav"))
#collision sound
cs=mixer.Sound(path.join(snd_dir,"blast.wav"))
cs2=mixer.Sound(path.join(snd_dir,"explosion.wav"))

class Player(pygame.sprite.Sprite):    #player sprite class
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)                  
        self.image=pygame.image.load(path.join(img_dir,"UIHere.png"))            
        self.rect=self.image.get_rect()                      
        self.rect.center=(300,710)
    def update(self):
        self.rect.x+=pxchange
        if self.rect.x<=5:
            self.rect.x=5
        if self.rect.x>=530:
            self.rect.x=530
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top,-10)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
            
class Enemy(pygame.sprite.Sprite):    #yellow alien sprite class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir,"enemy2.png"))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(600-self.rect.width)
        self.rect.y=random.randrange(-100,-70)
        self.speedy=2.3
        self.speedx=0
    def update(self):
        global gameove
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.right<=0 or self.rect.left>600:
            self.rect.x=random.randrange(600-self.rect.width)
            self.rect.y=random.randrange(-100,-70)
        if self.rect.y>660:
            gameove=True
class Enemy2(pygame.sprite.Sprite): #blue alien sprite class
    li=[150,100,500,450]
    lis=[2,2.02,1.8,1.9]
    lis2=[-2,-2.02,-1.8,-1.9]
    s=random.randint(0,3)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir,"enemy4.png"))
        self.rect=self.image.get_rect()
        self.rect.x=Enemy2.li[Enemy2.s]
        self.rect.y=random.randint(-100,-70)
        self.speedy=2
        if self.rect.x<400:
            self.speedx=Enemy2.lis[Enemy2.s]
        else:
            self.speedx=Enemy2.lis2[Enemy2.s]
    def update(self):
        global gameove
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        Enemy2.s=random.randint(0,3)
        if self.rect.right<=0 or self.rect.left>600:
            self.rect.x=Enemy2.li[Enemy2.s]
            self.rect.y=random.randrange(-100,-70)
            if self.rect.x<400:
                self.speedx=Enemy2.lis[Enemy2.s]
            else:
                self.speedx=Enemy2.lis2[Enemy2.s]
        if self.rect.y>660:
            gameove=True
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.bottom,10)
        all_sprites.add(bullet)
        bullets2.add(bullet)
        
class Enemy3(pygame.sprite.Sprite):    #red alien sprite class
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir,"enemy3.png"))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(250,350)
        self.rect.y=-40
        self.speedx=2*x
        self.speedy=2.3
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if  self.rect.left>=650 or self.rect.right<=0:
            self.rect.x=random.randrange(250,350)
            self.rect.y=-40
            
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.bottom,10)
        all_sprites.add(bullet)
        bullets2.add(bullet)        
            
      
        
        
class Bullet(pygame.sprite.Sprite): #bullet sprite class
    def __init__(self,x,y,z):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir,"beam.png"))
        self.image=pygame.transform.scale(self.image,(10,30))
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=z
        
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0 or self.rect.bottom>800:
            self.kill()

class Explosion(pygame.sprite.Sprite): #explosion sprite class
    
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=explosion_anim[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
        
    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>self.frame_rate:
            self.last_update=now
            self.frame+=1
            if self.frame==len(explosion_anim[self.size]):
                self.kill()
            else:
                center=self.rect.center
                self.image=explosion_anim[self.size][self.frame]
                self.rect=self.image.get_rect()
                self.rect.center=center
                
def pause():
    run=True
    while run:
        pause_word=font2.render("Game paused",True,(255,255,255))
        screen.blit(pause_word,(180,450))
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: 
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    run=False
        pygame.display.update()
score_value=0
def show_score():
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(480,10)) 


def show_title():
    title=font2.render("Space Invaders",True,(255,255,255))
    health=font.render("Hull",True,(255,255,255))
    screen.blit(health,(15,10))
    screen.blit(title,(170 ,620))
           
  
def game_over():
    screen.fill((0,0,0))
    over=font3.render("GAME OVER",True,(255,255,255))
    screen.blit(over,(100,330))
    score=font2.render("Score: "+str(score_value),True,(255,255,255))
    if s>score_value:
        hscore=font2.render("highscore:"+str(s),True,(255,255,255))
    else:
        hscore=font2.render("highscore:"+str(score_value),True,(255,255,255))
    screen.blit(score,(217,400))
    screen.blit(hscore,(180,440))
    for event in pygame.event.get():  
            if event.type==pygame.QUIT:   
                pygame.quit()
                sys.exit()

def fonts(x):
    return pygame.font.Font("freesansbold.ttf",x)
font=fonts(24)
font2=fonts(35)
font3=fonts(64) 
                                          
all_sprites=pygame.sprite.Group()
playerme=pygame.sprite.Group()
mobs=pygame.sprite.Group()
mobs2=pygame.sprite.Group()
mobs3=pygame.sprite.Group()
bullets=pygame.sprite.Group()
bullets2=pygame.sprite.Group()

player=Player()
all_sprites.add(player)
playerme.add(player)
xp=-1
for i in range(2):
    m=Enemy()
    m2=Enemy2()
    m3=Enemy3(xp)
    all_sprites.add(m)
    all_sprites.add(m2)
    all_sprites.add(m3)
    mobs.add(m)
    mobs2.add(m2)
    mobs3.add(m3)
m=Enemy()    
mobs.add(m)
all_sprites.add(m)

while True:
    #keep loop running a t the right speed
    clock.tick(90)
    #process events
    if gameove!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    pxchange=-3.5
                elif event.key==pygame.K_RIGHT:
                    pxchange=4
                elif event.key==pygame.K_SPACE:
                    if len(bullets)==0:
                        player.shoot()
                        bs.play()
                    if len(bullets2)==0:    
                        for i in mobs2:
                            i.shoot()
                        for i in mobs3:
                            i.shoot()
                elif event.key==pygame.K_p:
                    pause()
            elif event.type==pygame.KEYUP:
                if event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                        pxchange=0
         #update
        all_sprites.update()
        
        hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
        for hit in hits: 
            expl=Explosion(hit.rect.center,'lg')
            all_sprites.add(expl)
            cs.play()
            score_value+=1
            m=Enemy()
            all_sprites.add(m)
            mobs.add(m)
        hits2=pygame.sprite.groupcollide(mobs2,bullets,True,True)    
        for hit in hits2:
            expl=Explosion(hit.rect.center,'lg')
            all_sprites.add(expl)
            cs.play()
            score_value+=2
            m2=Enemy2()
            all_sprites.add(m2)
            mobs2.add(m2)    
        hits3=pygame.sprite.groupcollide(mobs3,bullets,True,True)
        for hit in hits3:
            expl=Explosion(hit.rect.center,'xlg')
            all_sprites.add(expl)
            cs.play()
            score_value+=3
            choice=random.randint(0,1)
            choice2=ly[choice]
            m3=Enemy3(choice2)
            all_sprites.add(m3)
            mobs3.add(m3)    
        hits5=pygame.sprite.groupcollide(playerme,bullets2,False,True)
        if len(hits5)>0:
            for hit in hits5:
                expl=Explosion(hit.rect.center,'lg')
                all_sprites.add(expl)
            cs2.play()
            x=x-1
        if x==0:
            if score_value>s:
                file2=open(path.join(img_dir,"game.txt"),"w")
                file2.write(str(score_value))
                file2.flush()
                file2.close()
            gameove=True
        #draw/ren
        relx=y%bg.get_rect().height
        screen.blit(bg,(0,relx-bg.get_rect().height))
        pygame.draw.rect(screen,(0,0,0),[70,10,155,25])
        pygame.draw.rect(screen,(0,255,0),[70,10,37.5*x,20])
        if relx<800:
            screen.blit(bg,(0,relx))
            pygame.draw.rect(screen,(0,0,0),[70,10,155,25])
            pygame.draw.rect(screen,(0,255,0),[70,10,37.5*x,20])
        y+=1.7
        pygame.draw.line(screen,(255,0,0),(0,660),(600,660))
        
        
        all_sprites.draw(screen)
        show_score()
        show_title()
        #after drawing,flip
        pygame.display.flip()
    else:
         game_over()
    pygame.display.update()    
         

        
            
    
        
        