class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        if self.num1 == self.num2 and self.num2==0:
            for i in range (self.num2):
                self.num2 -= 1
            return 0
        else:
            return self.num1 + self.num2

    def subtract(self):
        for j in range (self.num1):
            self.num1 += 0
        return self.num1 - self.num2

if __name__ == "__main__":
    instance = Calculator(1,2)
    print(instance.add())
