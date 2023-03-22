from turtle import Screen,Turtle
import winsound
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# window setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# when apple is eaten a sound is emitted
def eat_sound():
    winsound.PlaySound("bubble_pop_5.wav",winsound.SND_ASYNC)
def game_over_sound():
    winsound.PlaySound("game_over_sound.wav",winsound.SND_ASYNC)
    



# movement for the snake, using the arrow keys
screen.listen()
screen.onkeypress(key= "Up", fun= snake.move_up)
screen.onkeypress(key= "Down", fun= snake.move_down)
screen.onkeypress(key= "Left", fun= snake.move_left)
screen.onkeypress(key= "Right", fun= snake.move_right)
score_num = 0


# loop fo the movement of snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()    

# detect collision with food and change position of the food
    if snake.head.distance(food) < 15:
        food.new_position()
        score.increase_score()
        snake.extend()
        eat_sound()


# detect collision with wall  
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on =False
        score.game_over()
        game_over_sound()

# detect collision with own tail and end game, and sound is emitted, game over sound.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            game_over_sound()
        
        
    
        

screen.exitonclick()
