import turtle

def draw_bookshelf(x,y,width,height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def draw_book(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def draw_table(x,y):

    table_width = 100
    table_height = 50
    leg_height = 30

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(table_width)
    turtle.right(90)
    turtle.forward(table_height)
    turtle.right(90)
    turtle.forward(table_width)
    turtle.right(90)
    turtle.forward(table_height)
    turtle.right(90)    


def draw_lamp(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    # Draw stem
    turtle.penup()
    turtle.goto(x, y + 10)
    turtle.pendown()
    turtle.pensize(3)
    turtle.goto(x, y + 40)
    # Draw shade
    turtle.penup()
    turtle.goto(x - 20, y + 40)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(40)
        turtle.left(120)
    turtle.end_fill()
    turtle.pensize(1)

def draw_scene():

    turtle.speed(0)
    draw_bookshelf(-200, 0, 60, 180)

    shelf_y = [0, -60, -120]
    for y in shelf_y:
        for i in range(3):
            draw_book(-200 + 5 + i*18, y + 5, 15, 40)
    draw_table(50, -50)
    draw_lamp(100, -20)
    turtle.hideturtle()
    turtle.done()