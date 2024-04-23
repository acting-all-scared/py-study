import turtle as t
import random

def init(
        map_end:int=300, 
        target_location_band:int=150, 
        target_width:int=25, 
        canon_init_point:int=200):
    
    _map_vertical = 0    
    
    t.goto(map_end*-1, _map_vertical)
    t.down()
    t.goto(map_end, _map_vertical)

    #목표 지정 설정하고 그리기
    target = random.randint(target_location_band * -1, target_location_band)

    t.pensize(3)
    t.color("green")
    t.up()
    t.goto(target + (target_width * -1), 2)
    t.down()
    t.goto(target + target_width, 2)

    #거북이 색 검은색 처음 발사했던 곳으로 되돌립니다.

    t.color("black")
    t.up()
    t.goto(canon_init_point * -1,10)
    t.setheading(20)
    
    return target  # 생성된 target 값을 반환

def turn_up(): 
    t.left(2)

def turn_down(): 
    t.right(2)

def fire(target):
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)
    
    #while 반복문을 빠져나오면 거북이가 땅에 닿은 상태

    d = t.xcor() - target
    if abs(d) < 25:
        t.color("blue")
        t.write("Good!", False , "center", ("",15))

    else:
        t.color("red")
        t.write("Bad!!", False , "center", ("",15))
        t.color("black")
        t.goto(-200,10)
        t.setheading(ang)
        # 땅 그리기

def init_level(level:str='easy'):
    if level == 'easy':
        target = init(map_end=300, target_location_band=150, target_width=25, canon_init_point= 200)
    elif level == 'normal':
        target = init(map_end=400, target_location_band=200, target_width=5, canon_init_point= 300)
    else:
        target = init(map_end=400, target_location_band=200, target_width=5, canon_init_point= 300)
    return target

if __name__ == "__main__":
    target = init_level('normal')

    #거북이가 동작하는데 필요한 설정
    t.onkeypress(turn_up ,"Up")
    t.onkeypress(turn_down ,"Down")
    t.onkeypress(lambda: fire(target), "space")  # target 값을 fire 함수에 전달
    t.listen()
    t.mainloop()
