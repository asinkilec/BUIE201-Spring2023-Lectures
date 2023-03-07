i = 3
print (i)

def f():
    i = 9
    def g():
        nonlocal i
        i = 88
    print (i)
    g()

f()
del(i)
print (i)
f()