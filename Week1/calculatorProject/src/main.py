# import sys
# sys.path.append("D:\Python\self\my-learning-projects\Week1\calculatorProject")

from src.dataProcessing import Calculator, FileHandler

class CalcApp:
    def __init__(self):
        self.calc = Calculator()
        self.file = FileHandler()

    def run(self):
        while True:
            print("""\n ---Simple Calculator--- \n
                Choose your Operation\n
                1. Add\n
                2. Subtract\n
                3. Multiply \n
                4. Divide \n
                5. Square Root \n
                6. Power\n
                7. Show Previous results \n
                8. Clear Previous results \n
                9.Exit\n
                """
                  )
            choice = int(input("Enter your Choice(1-9) : "))
            if choice == 9:
                print("Exiting")
                break
            if choice == 8:
                self.file.clearData()
                print("Data Cleared")
                break
            if choice == 7:
                past_data = self.file.readData()
                if not past_data:
                    print("No past results fount")
                else:
                    print("\n past entries \n")
                    for line in past_data:
                        print(line.strip())
                continue
            try:
                if choice != 5:
                    a = float(input("Enter your first number: "))
                    b = float(input("Enter your second number:"))
                    if choice == 1:
                        result = self.calc.add(a,b)
                        operation = f"{a} + {b} : {result}"
                    elif choice == 2:
                        result = self.calc.sub(a, b)
                        operation = f"{a} - {b} : {result}"
                    elif choice == 3:
                        result = self.calc.mul(a, b)
                        operation = f"{a} * {b} : {result}"
                    elif choice == 4:
                        result = self.calc.div(a, b)
                        operation = f"{a} / {b} : {result}"
                    elif choice == 6:
                        result = self.calc.pwr(a, b)
                        operation = f"{a} ** {b} : {result}"
                elif choice == 5:
                    x = float(input("Enter your number "))
                    result = self.calc.sqrt(x)
                    operation = f"sqrt({x}) : {result}"
                else:
                    print("Invalid choice try again")
                    continue
                print(f"operation: {operation}")
                self.file.savedata(operation)
            except Exception as e:
                print(f"Error : {e}")


if __name__ == "__main__":
    app = CalcApp()
    app.run()
