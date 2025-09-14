
import turtle
import time
import random

# إعداد نافذة اللعبة
window = turtle.Screen()
window.title("لعبة الدودة (Snake)")
window.bgcolor("#22223b")  # لون خلفية جميل
window.setup(width=600, height=600)
window.tracer(0)

# رسم الحدود
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(4)
border.color("#f2e9e4")
border.penup()
border.goto(-290, 290)
border.pendown()
for _ in range(4):
    border.forward(580)
    border.right(90)

# رأس الدودة
head = turtle.Turtle()
head.shape("circle")  # شكل الرأس دائري
head.color("#4a4e69")
head.shapesize(stretch_wid=1.2, stretch_len=1.2)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# طعام الدودة
food = turtle.Turtle()
food.shape("circle")
food.color("#9a031e")
food.shapesize(stretch_wid=0.9, stretch_len=0.9)
food.penup()
food.goto(0, 100)

segments = []
score = 0

# كتابة النقاط
score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.color("#f2e9e4")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 260)
score_writer.write(f"Points {score}", align="center", font=("Arial", 26, "bold"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# ربط الأزرار
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# ألوان جسم الدودة
body_colors = ["#f72585", "#b5179e", "#7209b7", "#560bad", "#480ca8"]

# الحلقة الرئيسية للعبة
while True:
    window.update()

    # الاصطدام مع الجدار
    if (head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        score_writer.clear()
        score_writer.write(f"النقاط: {score}", align="center", font=("Arial", 26, "bold"))

    # الاصطدام مع الطعام
    if head.distance(food) < 20:
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        color_index = len(segments) % len(body_colors)
        new_segment.color(body_colors[color_index])
        new_segment.shapesize(stretch_wid=1, stretch_len=1)
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        score_writer.clear()
        score_writer.write(f"النقاط: {score}", align="center", font=("Arial", 26, "bold"))

    # تحريك جسم الدودة
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # الاصطدام مع الجسم
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            score_writer.clear()
            score_writer.write(f"النقاط: {score}", align="center", font=("Arial", 26, "bold"))

    time.sleep(0.09)

window.mainloop()
