import time
import random

operators = ["+", "-", "*"]
max_operand = 12
min_operand = 2
total_problems = 10 

def generateProblem(): 
    left = random.randint(min_operand, max_operand) 
    right = random.randint(min_operand, max_operand) 
    operator = random.choice(operators) 

    expression = str(left) + "" + operator + "" + str(right) 
    answer = eval(expression) #evaulate the randomly generated expression as if it was a python expression
    return expression, answer 

wrong = 0 

input("Press enter to start!") 
print("-------------------------") 

start_time = time.time() 

for i in range(total_problems): 
    expression, answer = generateProblem() 
    while True: 
        guess = input("Problem #" + str(i + 1) + ": " +  expression + " = ")
        if guess == str(answer): 
            break 

end_time = time.time()
total_time = end_time - start_time

print("------------------------") 
print("Nice work! You finished in " + str(round(total_time)) + " seconds!") 
                      



