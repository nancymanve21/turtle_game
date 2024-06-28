from turtle import Turtle, Screen
import random



is_game_on = False
screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
name_given = screen.textinput(title="Enter your name",prompt="Name")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")

    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y= y_position[index])
    new_turtle.color()
    all_turtles.append(new_turtle)


if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won {name_given}! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost {name_given}! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()