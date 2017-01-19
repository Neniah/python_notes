
x = 6

def example():
    z = 5
    print(z)

def example2():
    z = 7
    print(z)
    print(x)
    y = x + 10
    print(y)


example2()

def example3():
    global x
    x += 1
    print(x)
