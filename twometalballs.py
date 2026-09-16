import pgzrun
import random
WIDTH=800
HEIGHT=600
GRAVITY=2000.0

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


ball=Ball(50,100,40,"magenta")
def draw():
    screen.clear()
    ball.draw()

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

def on_key_down(key):
        if key==keys.SPACE:
            ball.vy=-500


pgzrun.go()