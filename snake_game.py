# projects
using python 3 
using by turtle 
import turtle
import time
import random

delay = 0.1

#set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Dharani")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #runs of the Screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Functions
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
        
def move():
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
def move():
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
#keyword bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
        
#main game loop
while True:
    wn.update()
    
    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        #clear the segments list
        segments.clear()
        
        #reset the Score
        score = 0
        
        #reset the delay
        delay = 0.1
        
        pen.clear()
        pen.write("score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))
    
    #check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randint(-299, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        #shorten the delay
        delay -= 0.001
        
        #increase the score
        score += 10
        
        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("score: {} High Score: {}".format(score, High_score), align="center",font=("courier", 24, "normal"))
        
    #Move the end segments first in reverse order
    for index in range(len(segments)-1, 0 , -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
    #move segment o to where the head is
    if len(segments) > 0:
        x = head.xcor()
        Y = head.ycor()
        segments[0].goto(x,y)
        
    move()
    
    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
                
            #clear the segments list
            segments.clear()
            
            #Reset the score
            score =0
            
            #Reset the delay
            delay = 0.1
            
            #update the score display
            pen.clear()
            pen.write("score: {} High Score: {}".format(score, High_score), align="center",font=("courier", 24, "normal"))
            
    
    time.sleep(delay)

wn.mainloop()
