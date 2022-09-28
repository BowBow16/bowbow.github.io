import turtle

wn = turtle.Screen()
wn.title("paanokung")
wn.bgcolor("white")
wn.setup(width=800, height=800)
wn.tracer(0)

#picture
picture = turtle.Turtle()
picture.image("download.jpg")


#loop
while True:
    wn.update()

