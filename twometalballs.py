import pgzrun
import random
WIDTH=800
HEIGHT=600
GRAVITY=2000.0
r=random.randint(255,255)
g=random.randint(0,200)
b=random.randint(100,200)
r1=random.randint(250,255)
g1=random.randint(0,200)
b1=random.randint(100,200)
r2=random.randint(250,255)
g2=random.randint(0,200)
b2=random.randint(100,200)
size=random.randint(20,100)
size1=random.randint(20,100)
size2=random.randint(20,100)
jump=random.randint(-701,-200)
jump1=random.randint(-701,-200)
jump2=random.randint(-701,-200)

class Ball:
    def __init__(self,initial_x,initial_y,initial_rad,initial_color):
        pass
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=initial_rad
        self.color=initial_color

    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos, self.radius,self.color)
       

ball=Ball(750,100,(size),(r,g,b))
ball2=Ball(50,100,(size1),(r1,g1,b1))
ball3=Ball(400,80,(size2),(r2,g2,b2))
def draw():
    screen.clear()
    ball.draw()
    ball2.draw()
    ball3.draw()

def update(dt):
    #Apply constantt acceleration formulae
    uy=ball.vy
    ball.vy+=GRAVITY * dt
    ball.y+=(uy+ball.vy)*0.5*dt

    if ball.y>HEIGHT:
        ball.y=HEIGHT-ball.radius
        ball.vy=-ball.vy*0.9
    uy=ball.vy+GRAVITY*dt
    ball.vy+=GRAVITY*dt
    ball.y+=(uy+ball.vy)*0.5*dt
    ball.x+=ball.vx*dt

    if ball.x>WIDTH:
        ball.vx=-ball.vx
    if ball.x<0:
        ball.vx=-ball.vx

#2nd ball
    uy=ball2.vy
    ball2.vy+=GRAVITY * dt
    ball2.y+=(uy+ball2.vy)*0.5*dt
    
    if ball2.y>HEIGHT:
        ball2.y=HEIGHT-ball2.radius
        ball2.vy=-ball2.vy*0.9
    uy=ball2.vy+GRAVITY*dt
    ball2.vy+=GRAVITY*dt
    ball2.y+=(uy+ball2.vy)*0.5*dt
    ball2.x+=ball2.vx*dt
    
    if ball2.x>WIDTH:
            ball2.vx=-ball2.vx
    if ball2.x<0:
            ball2.vx=-ball2.vx
#THIRD BALL
    uy=ball3.vy
    ball3.vy+=GRAVITY * dt
    ball3.y+=(uy+ball3.vy)*0.5*dt
    
    if ball3.y>HEIGHT:
        ball3.y=HEIGHT-ball3.radius
        ball3.vy=-ball3.vy*0.9
    uy=ball3.vy+GRAVITY*dt
    ball3.vy+=GRAVITY*dt
    ball3.y+=(uy+ball3.vy)*0.5*dt
    ball3.x+=ball3.vx*dt
    
    if ball3.x>WIDTH:
            ball3.vx=-ball3.vx
    if ball3.x<0:
            ball3.vx=-ball3.vx

def on_key_down(key):
        if key==keys.SPACE:
            ball.vy=jump
        if key==keys.UP:
             ball2.vy=jump1
        if key==keys.W:
             ball3.vy=jump2


pgzrun.go()
