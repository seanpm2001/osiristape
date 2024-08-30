import turtle

def draw_pikachu():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Pikachu Drawing")
    screen.bgcolor("white")

    # Create a turtle object
    pikachu = turtle.Turtle()
    pikachu.speed(3)

    # Drawing Pikachu's face
    pikachu.penup()
    pikachu.goto(0, -100)
    pikachu.pendown()
    pikachu.color("yellow")
    pikachu.begin_fill()
    pikachu.circle(100)
    pikachu.end_fill()

    # Drawing Pikachu's eyes
    pikachu.penup()
    pikachu.goto(-40, 0)
    pikachu.pendown()
    pikachu.color("black")
    pikachu.begin_fill()
    pikachu.circle(20)
    pikachu.end_fill()

    pikachu.penup()
    pikachu.goto(40, 0)
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.circle(20)
    pikachu.end_fill()

    # Drawing Pikachu's cheeks
    pikachu.penup()
    pikachu.goto(-70, -30)
    pikachu.pendown()
    pikachu.color("red")
    pikachu.begin_fill()
    pikachu.circle(30)
    pikachu.end_fill()

    pikachu.penup()
    pikachu.goto(70, -30)
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.circle(30)
    pikachu.end_fill()

    # Drawing Pikachu's mouth
    pikachu.penup()
    pikachu.goto(-30, -60)
    pikachu.pendown()
    pikachu.right(90)
    pikachu.circle(30, 180)

    # Finish drawing
    pikachu.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_pikachu()
