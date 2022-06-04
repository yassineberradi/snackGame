from turtle import Screen
from Snack import Snack
from Food import Food
from Score import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Screen")
screen.tracer(0)

snack = Snack()
food = Food()
score = Score()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")

snack.create_snack()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.add_segment(food.pos())
        score.increase_score()
    if snack.head.xcor() > 290 or snack.head.ycor() > 290 or snack.head.xcor() < -290 or snack.head.ycor() < -290:
        score.game_over()
        game_is_on = False
    for tl in snack.segments[1:]:
        if snack.head.distance(tl) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
