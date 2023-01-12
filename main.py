from turle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
  turtle.forward(10)



screen.listen()

turtle.onkey(key="space", fun=move_forwards)

screen.exitonclick()