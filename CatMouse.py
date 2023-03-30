import sys, pygame

pygame.init()

class House:
    def __init__(self):
        self._animals = []
        self._animals.append(Cat(1, 1))
        self._animals.append(Mouse(1, 1))
        self._animals.append(Mouse(1, 1))

    def Play(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()

            self._timeTick()
            self._clock.tick()

    def _timeTick(self):
        for a in self._animals:
            a.move()

        animal_pairs = [(a, b) for idx, a in enumerate(self._animals) for b in self._animals[idx + 1:]]

        caught_animals = []
        for (a, b) in animal_pairs:
            if a.check_if_you_caught(b):
                caught_animals.append(b)

        for a in caught_animals:
            a.die();        

class Animal:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self):
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
         
    def are_you_a_target_at_location(self, x, y):
        return self._x == x and self._y == y


class Cat(Animal):
    def __init__(self, x, y):
         super().__init__(x, y)
    
    def check_if_you_caught(self, a):
        return a.are_you_a_target_at_location(self._x, self._y)


h = House()
h.Play()
