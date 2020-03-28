import turtle

caro = turtle.Pen()
caro.shape("turtle")
caro.reset()
caro.speed(0)
a = 0
b = 1
for i in range(1, 15, 1):
    print(a)
    caro.forward(a)
    caro.left(90)
    c = a + b
    a = b
    b = c
    
