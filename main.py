import turtle
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True


def start_game():
    global game_on
    if screen.textinput("Restart Game?", "yes/no: ") == 'yes':
        snake.reset()
    else:
        game_on = False
    turtle.listen()
    score.reset()


while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        start_game()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            start_game()

    # detect collision with food
    if snake.head.distance(food) < 20:
        score.increase_score()
        score.update()
        snake.extend()
        food.refresh()

screen.exitonclick()
