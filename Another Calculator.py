# defining the addition function
def add(x, y): 
    return (x + y)

# defining the subraction function
def subtract(x, y): 
    return (x - y) 

# defining the multiplication function
def multiply(x, y): 
    return (x * y)

# defining the division function
def divide(x, y): 
    return round(x / y, 2)


while True:
    print("What operation would you like to do?\nAdd = 1\nSubract = 2\nMultiply = 3\nDivide = 4") 
    operator = input("Enter the operator number: ") 

    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    if operator == "1":
        print("Answer is: ", add(x, y))
    elif operator == "2": 
        print("Answer is: ", subtract(x, y))
    elif operator == "3":
        print("Answer is: ", multiply(x, y))
    elif operator == "4": 
        print("Answer is: ",  divide(x, y))
    
    ask_another = input("Do you have another calculation? (y/n): ")
    if ask_another.lower() == "n":
        break

print("bye :)")