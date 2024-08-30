import turtle as t
from PIL import Image

def draw_pikachu():
    # Set up screen and turtle
    screen = t.Screen()
    screen.setup(width=600, height=600)

    
    # Hide the turtle and speed up the drawing
    t.hideturtle()
    t.speed(9)
    
    # Example: Drawing Pikachu's head and ears (you can add more details)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.begin_fill()
    t.goto(-100, 150)
    t.goto(0, 200)
    t.goto(100, 150)
    t.goto(50, 50)
    t.end_fill()
    
    # Finish drawing and save the image
    screen.getcanvas().postscript(file="pikachu.eps")  # Save as an EPS file

    # Convert EPS to PNG using Pillow
    img = Image.open("pikachu.eps")
    img.save("docs/pikachu.png")

    # Clean up
    t.bye()

if __name__ == "__main__":
    draw_pikachu()
