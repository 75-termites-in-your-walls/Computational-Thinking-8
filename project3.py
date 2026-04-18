import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO- add starting values for all the main variables

x1 = -180
y1 = 120
x2 = -180
y2 = 80
x3 = -180
y3 = 30
x4 = -180
y4 = 50

# Section 2 - Setup

set_background("cornfield")
t1 = create_sprite("rocket",x1,y1)
t2 = create_sprite("red_tailed_hawk",x2,y2)
t3 = create_sprite("pinetree",x3,y3)
t4 = create_sprite("rock_climbers2",x4,y4)

# # Section 3 - Racing
#the rocket might lose sometimes because of lack of fuel.
for i in range(30):
    x1 +=random.randint(0,15)
    x2 +=(10)
    x3 +=(0)
    x4 +=random.randint(5,15)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)


#the falcon or the rocket win,depending on the rocket gets a higher speed factor than the falcon
# # Section 4 - Winner
# s5 = create_sprite("مَلِك܀غيف.gif",-200,-200)


if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
# line 47 and 48 are perfect, lines 5- - 56 all need to be fixed a little
elif x2 >= x1 and x2 >= x3 and x3 >= x4:
    print("player 2 wins!")

if x3 >= x1 and x3 >= x2 and x3 >= x4:
 print("player 4 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
 print("player 3 wins!")


turtle.exitonclick()

