import turtle
from colorsys import hsv_to_rgb

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Psychedelic Star")
screen.tracer(0)  # Turn off automatic screen updates for max speed

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

# Parameters for the drawing
num_layers = 15
num_lines_per_layer = 120
initial_radius = 200
hue_start = 0.6  # Start with a blue/purple hue

# Main drawing loop
for layer in range(num_layers):
    hue = (hue_start + (layer * 0.03)) % 1.0  # Cycle through hues
    
    for i in range(num_lines_per_layer):
        # Set the color for the current line
        rgb_color = hsv_to_rgb(hue, 1.0, 1.0)
        pen.pencolor(rgb_color)

        # Draw a line from the center outwards
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        
        # Calculate the angle and move the turtle
        pen.setheading(i * (360 / num_lines_per_layer))
        pen.forward(initial_radius - (layer * 12))

    screen.update() # Update the screen after each layer is drawn

# Keep the window open
turtle.done()