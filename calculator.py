def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "f{b} can't be zero, cannot divide by zero!"
    return a / b


if __name__ == "__main__":
    print("----- Simple Calculator ------")
    print("Addition : ", add(10,29))
    print("Subtraction : ", subtract(48,574))
    print("Multiplication : ", multiply(785,594))
    print("division : ", divide(475,57848))

print("hello github actions\n for testing github actions on push")

