
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to dark
screen.title("Colorful Bold Letter A")

# Set up the turtle
t = turtle.Turtle()
t.pensize(20)  # Increase the line thickness to make it bolder
t.speed(1)  # Set speed for animation

# Draw the left leg of 'A' with red color
t.penup()
t.goto(-100, -100)  # Move the turtle to a starting position
t.pendown()
t.color("red")
t.left(75)  # Start drawing the left leg of A
t.forward(200)

# Draw the right leg of 'A' with blue color
t.color("red")
t.right(150)  # Draw the right leg of A
t.forward(200)

# Draw the middle bar of 'A' with green color
t.color("red")
t.backward(100)  # Move halfway back to draw the middle bar
t.right(105)  # Draw the horizontal bar in the middle
t.forward(55)

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
