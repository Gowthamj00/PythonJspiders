# Python Program to Create a Class which Performs Basic Calculator Operations 
class BasicCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error! Division by zero."

    def equals(self):
        return self.a == self.b


# --- Main Program ---
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

bc1 = BasicCalculator(a, b)

while True:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Equals Check")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("Result:", bc1.addition())
    elif choice == "2":
        print("Result:", bc1.subtraction())
    elif choice == "3":
        print("Result:", bc1.multiplication())
    elif choice == "4":
        print("Result:", bc1.division())
    elif choice == "5":
        print("Are they equal?", bc1.equals())
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
