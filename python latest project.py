from turtle import *

shape("turtle")
speed(0)


def tree(size, levels, angle):
    if levels == -2:
        color("magenta")
        dot(size)
        color("brown")
        return

    forward(size)
    right(angle)

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)


def snowflake_side(length, levels):
    if levels == 0:

        back(length)
        return

    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)


def create_snowflake(sides, length):
    colors = ["cyan", "cyan", "cyan", "cyan"]
    for i in range(sides):
        color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)



color('orange', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()



left(90)
tree(70, 7, 40)

create_snowflake(4,150)

mainloop()