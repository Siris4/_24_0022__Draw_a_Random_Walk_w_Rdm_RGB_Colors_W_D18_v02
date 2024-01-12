import turtle as t  #we have to change the actual turtle Module, not the object
import random
from turtle import Screen

tiptup = t.Turtle()

tiptup.speed('fastest')

t.colormode(255)


# r = ""
# g = ""
# b = ""
# rgb = ""

#TODO 1: Thickness of the paint
tiptup.pensize(width=4)
tiptup.width(width=4)

movement_list = [90, 180, 270, 360]

def random_color_generator():
    # global r, g, b, rgb
    # (r, g, b) = ""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color

# print(rgb)

def move_in_a_random_direction():
    tiptup.right(random.choice(movement_list))
    tiptup.forward(25)


#TODO 2: Speed that it "walks"

for _ in range(350):
    tiptup.color(random_color_generator())
    #rgb(168, 145, 0)
    move_in_a_random_direction()

screen = Screen()
screen.exitonclick()