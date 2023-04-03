import sys, pygame

pygame.init()

class House:
    def __init__(self):
<<<<<<< Updated upstream
        self._animals = []
        self._animals.append(Cat(1, 1))
        self._animals.append(Mouse(1, 1))
=======
        self._animals = [] #constructer
        self._animals.append(Cat(1, 1)) #Cat classinda tahmini 3 parameter var. additionally self. MIDTERMDE BOLE BISI SORCAK
        self._animals.append(Mouse(1, 1)) #polymorphismin olmadigi tek yer bu uc satir. cat mi mouse mu soylememiz lazim
>>>>>>> Stashed changes
        self._animals.append(Mouse(1, 1))

    def Play(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()

<<<<<<< Updated upstream
            self._timeTick()
            self._clock.tick()
=======
            self._timeTick() #timetick de clock da oyun icinde cagirilan fonksiyonlar
            self._clock.tick() #ondan dolayi ikisi de private variable, DATA HIDING!!
>>>>>>> Stashed changes

    def _timeTick(self):
        for a in self._animals:
            a.move()

        animal_pairs = [(a, b) for idx, a in enumerate(self._animals) for b in self._animals[idx + 1:]]

        caught_animals = []
        for (a, b) in animal_pairs:
            if a.check_if_you_caught(b):
                caught_animals.append(b) #polymorphism. objectin sadece animal oldugunu bilmemiz yeterli.

        for a in caught_animals:
            a.die();        

class Animal:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self): #_move degil demek ki disardan cagirabiliyoz
        pass

    def die(self):
        pass

    def die(self):
        pass    

    def are_you_a_target_at_location(self, x, y):
        return False
    
    def check_if_you_caught(self, a):
        return False

class Mouse(Animal):
    def __init__(self, x, y):
         super().__init__(x, y)
<<<<<<< Updated upstream
         
=======

>>>>>>> Stashed changes
    def are_you_a_target_at_location(self, x, y):
        return self._x == x and self._y == y


class Cat(Animal):
    def __init__(self, x, y):
         super().__init__(x, y)
    
    def check_if_you_caught(self, a):
        return a.are_you_a_target_at_location(self._x, self._y)


h = House()
h.Play()
