import turtle as t
import random

score = 0
playing = False #현재 게임이 플레이 중인지 확인하는 변수


#악당 거북이
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

#먹이
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

#turn_
def turn_up():
    t.setheading(90)
def turn_right():
    t.setheading(0)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)

#play(게임시작) 함수

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()


#게임을 실제로 플레이 함수

def play():
    global score
    global playing
    t.fd(10)
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5

    if speed >15:
        speed = 15
    te.forward(speed)
    if t.distance(te) < 12 :

        text = "score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if t.distance(ts) < 12:
        score = score + 1
        t.write(score)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x,star_y)
    if playing:
        t.ontimer(play, 100)

#메세지 화면에 표시하는 함수

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0,- 100)
    t.write(m2, False, "center", ("",20))
    t.home()


#게임준비

t.title("Turtle Run")
t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.color("white")
t.speed(0)
t.up()

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start," space")

t.listen()
message("Turtle Run", "[space]")
t.mainloop()
