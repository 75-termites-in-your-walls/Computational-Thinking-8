# Section 1 - Your code
from utils import *
set_background("capybara_sunset")

s1 = create_sprite("mario", 100, 100)
s2 = create_sprite("kitten", -100, 100)
s2 = create_sprite("sodacan", -100, -100)
s2 = create_sprite("rocket", 100, -100)

message1 = create_sprite("basketball",-200,200)
message1.color("purple")
message1.write("get the spaghetti",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()