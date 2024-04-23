import turtle as t
import random

#악당 거북이
te = t.Turtle()
te.shape("turtle")
te.color('red')
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

score = 0


#turn_으로 시작하는 함수
def turn_up():
    t.setheading(90)
def turn_right():
    t.setheading(0)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)

# 점수 표시 함수
def display_score():
    t.undo()  # 이전에 그려진 점수 텍스트 지우기 /중복해서 겹쳐서 나옴
    t.penup()  # 펜을 들어서 이동하기
    t.goto(200, 200)  # 텍스트를 표시할 위치로 이동
    text = f"점수: {score}"  # 점수 문자열 생성
    t.write(text, align="right", font=("Arial", 16, "normal"))  # 텍스트 표시

#play 함수
#주인공 거북이가 앞으로 이동, 악당 거북이 쫓아가기, 주인공 거북이 악당 또는 먹이 닿

def play():
    global score, food_pos
    t.forward(10)
    ang =te.towards(t.pos())
    te.setheading(ang)
    te.forward(9)
    if t.distance(ts) < 12:
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x,star_y)
        score += 10
        display_score() #점수 표시 함수 호출
       
    if score <100:
        t.ontimer( play, 100)


#게임 준비 및 실행
#화면 배경 그리기, 키보드 입력처리 하기, 


t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")

t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_up," Up")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down,"Down")


t.listen()
play()

t.mainloop()

