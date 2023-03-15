class Human:
    age = 33
    def __init__(self, namein, agein) -> None:
        self.name = namein
        self.age = agein

    def walk(self):
        print(self.name + " is walking.")

class Professor(Human):
      def __init__(self, namein, agein, salaryin) -> None:
        super().__init__(namein, agein)
        self.salary = salaryin

x = Professor("tamer", 1, 2)
print (x.age)
x.walk()

