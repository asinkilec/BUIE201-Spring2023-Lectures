def f(name):    
    for i in range(len(name)):
        for j in range(i, len(name)):
            ss = name[i:j+1]
            print(ss + "   " + str(sum([ord(s) for s in ss])))


f ("hello")