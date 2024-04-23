import tkinter as tk
from tkinter import ttk
import turtle as t
import random

score = 0
score_delta = 0
t.register_shape("rocket-joypixels.gif")
rockt_t = t.Turtle()
rockt_t.shape("rocket-joypixels.gif")

def init(
        map_end:int=300, 
        target_location_band:int=150, 
        target_width:int=25, 
        canon_init_point:int=200):
    
    _map_vertical = 0    
    
    rockt_t.goto(map_end*-1, _map_vertical)
    rockt_t.down()
    rockt_t.goto(map_end, _map_vertical)

    #목표 지정 설정하고 그리기
    target = random.randint(target_location_band * -1, target_location_band)

    rockt_t.pensize(3)
    rockt_t.color("green")
    rockt_t.up()
    rockt_t.goto(target + (target_width * -1), 2)
    rockt_t.down()
    rockt_t.goto(target + target_width, 2)

    #거북이 색 검은색 처음 발사했던 곳으로 되돌립니다.

    rockt_t.color("black")
    rockt_t.up()
    rockt_t.goto(canon_init_point * -1,10)
    rockt_t.setheading(20)
    
    return target  # 생성된 target 값을 반환

def turn_up(): 
    rockt_t.left(2)
    update_angle_display()

def turn_down(): 
    rockt_t.right(2)
    update_angle_display()

def fire(target):
    global score
    ang = rockt_t.heading()
    while rockt_t.ycor() > 0:
        rockt_t.forward(15)
        rockt_t.right(5)
    
    #while 반복문을 빠져나오면 거북이가 땅에 닿은 상태


    d = rockt_t.xcor() - target
    if abs(d) < 25:
        rockt_t.color("blue")
        rockt_t.write("Good!", False , "center", ("",15))
        rockt_t.color("black")
        rockt_t.goto(-200,10)
        rockt_t.setheading(ang)
        return "Good"  # Good!을 표시하고 게임을 끝

    else:
        rockt_t.color("red")
        rockt_t.write("Bad!!", False , "center", ("",15))
        rockt_t.color("black")
        rockt_t.goto(-200,10)
        rockt_t.setheading(ang)
        return "Bad"



def update_angle_display():
    ang = int(rockt_t.heading())
    canvas.delete("angle_text")  # 이전에 표시된 각도 텍스트 삭제
    canvas.create_text(canvas_width - 20, 50, text=f"Angle: {ang}", anchor="ne", fill="black", font=("Arial", 12), tags="angle_text")


def init_level(level:str='easy'):
    global score_delta
    update_score_display()
    update_angle_display()

    if level == 'easy':
        target = init(map_end=300, target_location_band=150, target_width=25, canon_init_point= 200)
        score_delta = 10

    elif level == 'normal':
        target = init(map_end=400, target_location_band=200, target_width=5, canon_init_point= 300)
        score_delta = 25

    elif level == 'hard':  # 'hard' 레벨에 대한 설정 추가
        target = init(map_end=500, target_location_band=250, target_width=10, canon_init_point= 400)
        score_delta = 50
    else:
        target = init(map_end=300, target_location_band=150, target_width=25, canon_init_point= 200)  # 기본값은 'easy'
        score_delta = 10
    return target

def update_score(game_result):
    global score
    if game_result == "Good":
        score += score_delta
    elif game_result == "Bad":
        score -= 10  # Bad일 때는 고정된 점수를 감소시킴
    update_score_display()

def start_game():
    selected_level = level_combobox.get()
    target = init_level(selected_level)

    #거북이가 동작하는데 필요한 설정
    t.onkeypress(turn_up ,"Up")
    t.onkeypress(turn_down ,"Down")
    t.onkeypress(lambda: update_score(fire(target)), "space")  # target 값을 fire 함수에 전달
    t.listen()
    rockt_t.mainloop()

# GUI 생성
root = tk.Tk()
root.title("Game Level Selection")

canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

level_label = ttk.Label(root, text="Select Game Level:")
level_label.pack(pady=10)

level_combobox = ttk.Combobox(root, values=["easy", "normal", "hard"])
level_combobox.pack(pady=5)
level_combobox.current(0)

start_button = ttk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

root.mainloop()
