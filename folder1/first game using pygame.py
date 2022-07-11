import pygame
import random
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE WAR")
i=pygame.image.load('warrior.png')
pygame.display.set_icon(i)
rock=[pygame.image.load("asteroid.png"),pygame.image.load("asteroid.png"),pygame.image.load("asteroid.png")]
hero=pygame.image.load("bullet.png")
enemy=[pygame.image.load("enemy.png"),pygame.image.load("enemy.png"),pygame.image.load("enemy.png")]
enemybullet=pygame.image.load("bullet (1).png")
galaxy=pygame.image.load("planet.png")
x=355
y=480
z=0
k=0
z1=0
z2=0
x1=[0,0,0]
y1=[-75,-75,-75]
x3=[0,0,0]
y3=[-100,-100,-100]
x4=[0,0,0]
y4=[-100,-100,-100]
y2=1
k1=0
speed=0
spe=0
access=[1,1,1]
prob=True
score=0
health=100
col=[0,0,0]
d=[0,0,0]
ro=[0,0,0]
s1=["ready","ready","ready"]
s2=["ready","ready","ready"]
s=0
start=0
pause=1
hi=1
file=open('highscore','r')
highscore=int(file.read())
file.close()
#mixer.music.load('Cinematic-electronic-track.mp3')
#mixer.music.play(-1)
def player(x,y):
    screen.blit(i,(x,y))
def rocks(x1,y1,i):
    screen.blit(rock[i],(x1,y1))
def abc(x3,y3,i):
    screen.blit(enemy[i],(x3,y3))
def bullet(x2,y2):
    screen.blit(hero,(x2,y2));
def bullet1(x2,y2):
    screen.blit(enemybullet,(x2,y2));
def collision1(x1,x2,y1,y2):
    amt=math.sqrt((math.pow(x2+10-x1-45,2))+(math.pow(y2-y1,2)))
    if amt<=40:
        return True
    else:
        return False
def collision2(x1,x2,y1,y2):
    amt=math.sqrt((math.pow(x2+10-x1-40,2))+(math.pow(y2-y1,2)))
    if amt<=40:
        return True
    else:
        return False
def collisionbul(x1,x2,y1,y2):
    amt=math.sqrt((math.pow(x2+7-x1-40,2))+(math.pow(y2-y1,2)))
    if amt<=45:
        bul_sound=mixer.Sound('bulhit.wav')
        bul_sound.play()
        return 1
    else:
        return 0
def collisionrock(x1,x2,y1,y2):
    amt=math.sqrt((math.pow(x2+35-x1-45,2))+(math.pow(y2-y1,2)))
    if amt<=65:
        rock_sound=mixer.Sound('Explosion+5.wav')
        rock_sound.play()
        return 1
    else:
        return 0
def collisionship(x1,x2,y1,y2):
    amt=math.sqrt((math.pow(x2+35-x1-45,2))+(math.pow(y2-y1,2)))
    if amt<=70:
        rock_sound=mixer.Sound('Explosion+5.wav')
        rock_sound.play()
        return 1
    else:
        return 0
def showhealth():
    font=pygame.font.Font("freesansbold.ttf",20)
    h=font.render("Health : " + str(health) + "%",True,(255,255,255))
    screen.blit(h,(650,0))
run=True
while run:
    screen.fill((0,0,0))
    if pause==0:
        font=pygame.font.Font("freesansbold.ttf",64)
        pa=font.render("PAUSED",True,(255,255,255))
        screen.blit(pa,(200,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pause=1
    if health<=0:
        font=pygame.font.Font("freesansbold.ttf",32)
        gameover=font.render("GAME OVER",True,(255,255,255))
        screen.blit(gameover,(200,250))
        gameover=font.render("YOUR SCORE : " + str(score),True,(255,255,255))
        screen.blit(gameover,(200,282))
        gameover=font.render("PRESS R TO RESTART",True,(255,255,255))
        high=score
        if high>highscore:
            highscore=high
            file=open('highscore','w')
            file.write(str(high))
            file.close()
        screen.blit(gameover,(200,314))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    health=100
                    x=355
                    y=480
                    z=0
                    k=0
                    z1=0
                    z2=0
                    x1=[0,0,0]
                    y1=[-75,-75,-75]
                    x3=[0,0,0]
                    y3=[-100,-100,-100]
                    x4=[0,0,0]
                    y4=[-100,-100,-100]
                    y2=1
                    k1=0
                    speed=0
                    spe=0
                    access=[1,1,1]
                    prob=True
                    score=0
                    health=100
                    col=[0,0,0]
                    d=[0,0,0]
                    ro=[0,0,0]
                    s1=["ready","ready","ready"]
                    s2=["ready","ready","ready"]
                    s=0
                    start=0
                    pause=1
                    break
    if start==0:
        if hi:
            font=pygame.font.Font("freesansbold.ttf",32)
            st=font.render("PRESS S TO START THE GAME",True,(255,255,255))
            screen.blit(st,(140,240))
            font=pygame.font.Font("freesansbold.ttf",32)
            hs=font.render("PRESS H TO VIEW HIGHSCORE",True,(255,255,255))
            screen.blit(hs,(140,390))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_s and hi:
                    start=1
                if event.key==pygame.K_h:
                    hi=0
                if event.key==pygame.K_BACKSPACE:
                    hi=1
                if event.key==pygame.K_DELETE and hi==0:
                    file=open('highscore','w')
                    file.write('0')
                    file.close()
                    highscore=0
        if hi==0:
            font=pygame.font.Font("freesansbold.ttf",32)
            css=font.render("HIGHSCORE : " + str(highscore),True,(255,255,255))
            screen.blit(css,(200,190))
            css=font.render("PRESS DELETE TO RESET",True,(255,255,255))
            screen.blit(css,(140,400))
    if health>0 and start and pause:
        speed+=1/10000
        spe+=1/50000
        if speed>=2.7:
            speed=2.7
        if spe>=2:
            spe=2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    z=-2
                if event.key == pygame.K_RIGHT:
                    z=2
                if event.key == pygame.K_UP:
                    z1=-2
                if event.key == pygame.K_DOWN:
                    z1=2
                if event.key==pygame.K_SPACE and s==0:
                    bul_sound=mixer.Sound('Cannon+5.wav')
                    bul_sound.play()
                    s=1
                    x2=x+45-12.5
                    y2=y
                if event.key==pygame.K_p:
                    pause=0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    z=0
                    z1=0
        for j in range(0,3):
            if s1[j]=="ready":
                x1[j]=random.randint(0,725)  
                s1[j]="not ready"
        z2=speed
        for j in range(0,3):
            if y1[j]>=675:
                y1[j]=-75
                s1[j]="ready"
            ro[j]=collisionrock(x,x1[j],y,y1[j])
            if ro[j]:
                y1[j]=-75
                s1[j]="ready"
                health-=20
        for j in range(0,3):
            if s2[j]=="ready":
                x3[j]=random.randint(0,725)
                s2[j]="not ready"
        for j in range(0,3):
            if y3[j]>=675:
                y3[j]=-100
                s2[j]="ready"
            d[j]=collisionship(x,x3[j],y,y3[j])
            if d[j]:
                y3[j]=-100
                s2[j]="ready"
                health-=20
        x+=z
        y+=z1
        for j in range(0,3):
            y1[j]+=z2
        for j in range(0,3):
            y3[j]+=spe
            if y3[j]>=720:
                y3[j]=-100
        if x>=800-90:
            x=800-90
        if x<=0:
            x=0
        if y>=600-90:
            y=600-90
        if y<=0:
            y=0
        if y2<=0:
            s=0
            y2=1
        if s:
            for j in range(0,3):
                a=collision1(x1[j],x2,y1[j],y2)
                if a==True:
                    rock_sound=mixer.Sound('Explosion+5.wav')
                    rock_sound.play()
                    s1[j]="ready"
                    y1[j]=-75
                    s=0
                b=collision2(x3[j],x2,y3[j],y2)
                if b==True:
                    ship_sound=mixer.Sound('Explosion+5.wav')
                    ship_sound.play()
                    s2[j]="ready"
                    y3[j]=-100
                    s=0
                    score+=10
                y2-=1.6
                bullet(x2,y2)
        c=0
        font=pygame.font.Font("freesansbold.ttf",32)
        scor=font.render("Score :" + str(score), True,(255,255,255))
        for j in range(0,3):
            rocks(x1[j],y1[j],c)
            c+=1
        c1=0
        for j in range(0,3):
            if access[j]:
                x3[j]+=0.9
            else:
                x3[j]-=0.9
            if x3[j]<=0:
                access[j]=1
            if x3[j]>=710:
                access[j]=0
            abc(x3[j],y3[j],c1)
            if prob==True:
                eb_sound=mixer.Sound('Gun+Silencer.wav')
                eb_sound.play()
                x4[j]=x3[j]+40
                y4[j]=y3[j]+80-7
                prob=False
            if prob==False:
                y4[j]+=1.2
                bullet1(x4[j],y4[j])
            if y4[j]>=644 and prob==False and y3[j]<450:
                eb_sound=mixer.Sound('Gun+Silencer.wav')
                eb_sound.play()
                y4[j]=y3[j]+80-7
                x4[j]=x3[j]+40
            if prob==False:
                col[j]=collisionbul(x,x4[j],y,y4[j])
                if col[j]:
                    l=0
                    while l<100000:
                        l+=1
                    y4[j]=644
                    health-=10
            c1+=1
        showhealth()
        player(x,y)
        screen.blit(scor,(0,0))
    pygame.display.update()
pygame.quit()

