from turtle import Turtle, Screen
from random import randint

screen = Screen()

keep_running = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
positions = [-90, -60, -30, 0, 30, 60, 90]
names = ["apollo", "viktor", "hunter", "gioo", "kami", "triz", "jean"]
number = 0

for turtle in range(7):
    names[number] = Turtle(shape="turtle")
    names[number].color(colors[number])
    names[number].penup()
    names[number].goto(x=-230, y=positions[number])
    number += 1

if user_bet:
    keep_running = True

while keep_running:
    for turtle_step in names:
        if turtle_step.xcor() > 230:
            winning_color = turtle_step.pencolor()

            if winning_color == user_bet:
                print(f"Congratulations, the {user_bet} turtle won the race! You chose the right one.")

            else:
                print(f"Sorry, but the {winning_color} turtle won the race. You chose the wrong one.")

            keep_running = False

        turtle_step.forward(randint(0, 10))

screen.exitonclick()