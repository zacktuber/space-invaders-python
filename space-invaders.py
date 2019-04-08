import turtle
import os
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("green")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for i, enemy in enumerate(enemies):
    enemy.color("green")
    enemy.shape("square")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-50 * i, 200)

enemyspeed = 3

bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20

bulletstate = "ready"


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    dx = t1.xcor()-t2.xcor()
    dy = t1.ycor()-t2.ycor()
    d = math.sqrt (math.pow(dx, 2)+ math.pow(dy, 2))
    return d < 20


wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                enemyspeed *= -1
                e.sety(y)

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                enemyspeed *= -1
                e.sety(y)

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemy.setposition(-200, 250)
            enemyspeed *= 1.1

    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



delay = raw_input("Press any key to finish")
