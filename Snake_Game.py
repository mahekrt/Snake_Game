# body collisions



import turtle    #Set up the screen
import time
import random
# making of the screen
delay = 0.1

#Score
score = 0
high_score = 0
wn = turtle.Screen()
wn.title("Snake Game by @Mahek")
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.tracer(0)  #turns off the screen updates(turns off the animation)


#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()    #for not drawing any lines or anything else
head.goto(0,0)   #starting it from the centre of the screen, basically turtlr module starts from side but its our choice
head.direction = "left"


#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()    #for not drawing any lines or anything else
food.goto(0,100)   #starting it from the centre of the screen, basically turtlr module starts from side but its our choice


#making list for snake body
segments = []


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0                 High Score:0", align="center", font=("Cambria", 20, "bold"))

# #Functions
def go_up():
    # if head.direction != "down":
        head.direction = "up"

def go_down():
    # if head.direction != "up":
        head.direction = "down"

def go_left():
    # if head.direction != "right":
        head.direction = "left"

def go_right():
    # if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "u")
wn.onkeypress(go_down, "i")
wn.onkeypress(go_left, "o")
wn.onkeypress(go_right, "p")


# Main game loop
while True:
    wn.update()

   #check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
#
#
#         # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

         #Clear the segments list
        segments.clear()

#         #reset the score
        score = 0
#
#         #reset the delay
#         delay = 0.1u
#
        pen.clear()
        pen.write("Score: {}         High Score:{}".format(score, high_score), align="center", font=("Cambria", 20, "bold"))
#
    #checking for collision of food and head of the snake
    if head.distance(food) < 20:
        #Move the food to the random spot on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
#
#
        #Add a segment(body of the snake)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)
#
         #shorten the delay
        # delay = 0.001
#
         #increase the score
        score += 10
#
#
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write("Score: {}           High Score:{}".format(score, high_score), align="center", font=("Cambria", 20, "bold"))
#
#     #Move the last segment to the first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

#     #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
#
#     # check for body collision with the body segments
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
#
#             # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
#
#             # Clear the segments list
            segments.clear()
#
#             # reset the score
            score = 0
#
#             #reset the delay
#             delay = 0.1
#
#             #update the score
            pen.clear()
            pen.write("Score: {}                        High Score:{}".format(score, high_score), align="center", font=("Cambria", 20, "bold"))

    time.sleep(delay)


wn.mainloop()
