import turtle as t
from PIL import Image

def draw_pikachu():
    # Set up screen and turtle
    screen = t.Screen()
    screen.setup(width=600, height=600)
 
    # ... (rest of the code to draw Pikachu) ...
    # Ears
    t.penup()
    t.goto(-100, 150)
    t.pendown()
    t.begin_fill()
    t.color("yellow")
    t.circle(50, 180)
    t.end_fill()

    t.penup()
    t.goto(100, 150)
    t.pendown()
    t.begin_fill()
    t.circle(50, 180)
    t.end_fill()

    # Head
    t.penup()
    t.goto(-60, 100)
    t.pendown()
    t.begin_fill()
    t.circle(120)
    t.end_fill()

    # Eyes
    t.penup()
    t.goto(-60, 100)
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.circle(25)
    t.end_fill()

    t.penup()
    t.goto(60, 100)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.penup()
    t.goto(-45, 110)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(75, 110)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Nose
    t.penup()
    t.goto(15, 70)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Mouth
    t.penup()
    t.goto(-25, 50)
    t.pendown()
    t.right(90)
    t.circle(20, 180)

    t.penup()
    t.goto(-25, 50)
    t.pendown()
    t.left(180)
    t.circle(-20, 180)

    # Cheeks
    t.penup()
    t.goto(-75, 55)
    t.pendown()
    t.begin_fill()
    t.color("red")
    t.circle(25)
    t.end_fill()

    t.penup()
    t.goto(85, 55)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.hideturtle()
    t.done()


    # Finish drawing and save the image
    screen.getcanvas().postscript(file="pikachu.eps")  # Save as an EPS file

    # Convert EPS to PNG using Pillow
    img = Image.open("pikachu.eps")
    img.save("docs/pikachu.png")

    # Clean up
    t.bye()

if __name__ == "__main__":
    draw_pikachu()
