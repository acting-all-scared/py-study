import turtle as t

# 화살표 이미지 등록
t.register_shape("rocket-joypixels.gif")

# 거북이 생성 및 모양 설정
arrow_turtle = t.Turtle()
arrow_turtle.shape("rocket-joypixels.gif")

# 거북이 이동 및 동작
arrow_turtle.forward(100)
arrow_turtle.left(90)

# 화면 유지
t.mainloop()
