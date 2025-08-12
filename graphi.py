[]
import turtle
import random

# --- Setup the Environment ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Slow-Growing Fractal Tree")
# We remove screen.tracer(0) to re-enable animation

pen = turtle.Turtle()
pen.hideturtle()
pen.setheading(90)  # Point the turtle upwards
pen.color("white")

# --- Speed Control ---
# Set speed to a visible level. '0' is fastest, '10' is fast, 
# '6' is normal, '3' is slow, '1' is slowest.
pen.speed(7) # A good speed to watch it grow

# --- The Recursive Drawing Function ---
def draw_branch(branch_length, pen_size):
    # Base case: Stop when the branches are too short
    if branch_length < 15:
        # Draw a "leaf" at the end of the branch
        pen.color(random.choice(["spring green", "lawn green", "green yellow"]))
        pen.stamp() # Stamp a turtle shape as a leaf
        pen.color("saddle brown")
        return

    # --- Draw the main branch ---
    pen.pensize(pen_size)
    pen.color("saddle brown")
    pen.forward(branch_length)

    # --- Recursive Step: Create two new smaller branches ---
    new_length = branch_length * random.uniform(0.7, 0.9)
    right_angle = random.randint(15, 35)
    left_angle = random.randint(15, 35)

    # 1. First branch (right)
    pen.right(right_angle)
    draw_branch(new_length, pen_size * 0.7)

    # 2. Second branch (left)
    pen.left(right_angle + left_angle) # Turn left from the original branch angle
    draw_branch(new_length, pen_size * 0.7)

    # --- Backtrack to the original position ---
    pen.right(left_angle)
    pen.backward(branch_length)

# --- Initial Call to Start the Drawing ---
pen.penup()
pen.goto(0, -300)
pen.pendown()

# Start the recursion
draw_branch(120, 10)

# Keep the window open after drawing is complete
turtle.done()