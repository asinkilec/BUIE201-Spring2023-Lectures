i = 88
class Apple:
    def __init__(self, k) -> None:
        self.g = k
 
    i = 99
    def f(self, h):
        self.j = h
        print (self.j)
    
x = Apple(12)
y = Apple(35)
x.f(55)
#Apple.f(x, 55)

y.f(77)
#Apple.f(y, 77)

print (x.j)
