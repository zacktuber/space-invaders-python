import turtle
import os
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Gnome Invaders")
wn.bgpic("background.gif")

wn.register_shape("mabel80.gif")
wn.register_shape("gnome.gif")
wn.register_shape("hook.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("#654321")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_pen.hideturtle()
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

player = turtle.Turtle()
player.color("blue")
player.shape("mabel80.gif")
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
    enemy.shape("gnome.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-50 * i, 200)

enemyspeed = 3

bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("hook.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.setposition(0,-300)
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
        os.system("afplay grapplinghook.m4a&")
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

def printGameOver():
    os.system("afplay riggedit.m4a&")
    go_pen = turtle.Turtle()
    go_pen.speed(0)
    go_pen.color("red")
    go_pen.penup()
    go_pen.setposition(0, 0)
    go_pen.hideturtle()
    go_pen.write("GAME OVER DUDE!", False, align="center", font=("Arial", 40, "bold"))


wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

gameover=False

while not gameover:
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
            os.system("afplay wowcool.m4a&")
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemy.setposition(-200, 250)
            enemyspeed *= 1.1
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(enemy, player):
            gameover = True

        if enemy.ycor() < -250:
            gameover = True


    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


printGameOver()
delay = raw_input("Press any key to finish")
