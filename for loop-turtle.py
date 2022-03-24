Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.speed(100)
turtle.bgcolor('black')

for i in range(90):
    t.color('cyan')
    t.circle(i)
    t.left(5)

    
import turtle
t = turtle.Pen()
t.shape('turtle')
t.color('green')
t.left(90)
t.speed(100)
def tree(i):
    if i<6:
        return
    else:
        t.forward(i)
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)

        
tree(90)
