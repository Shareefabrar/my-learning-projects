import math


class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("can't be divided by 0")
        return a / b

    def sqrt(self, a):
        if a <= 0:
            raise ValueError("number should be greater than 0")
        return math.sqrt(a)

    def pwr(self, a, b):
        return a ** b
    

class FileHandler:
    def __init__(self, filename="./data/results.txt"):
        self.filename = filename

    def savedata(self, expression):
        with open(self.filename, "a") as f:
            f.write(f"{expression}\n")

    def readData(self):
        try:
            with open(self.filename, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def clearData(self):
        open(self.filename, "w").close()
