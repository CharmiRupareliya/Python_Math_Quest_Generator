import random
import time
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

OPERATORS = ["+", "*", "-"]
MIN_OPRAND = 3
MAX_OPRAND = 12
TOTAL_PROBLEMS = 10
def genrate_problem():
    left = random.randint(MIN_OPRAND, MAX_OPRAND)
    right = random.randint(MIN_OPRAND, MAX_OPRAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)

    return expr, answer

wrong = 0
print()
input(Fore.MAGENTA + Style.BRIGHT + f"Press Enter to Start!")
print(Fore.MAGENTA + f"--------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = genrate_problem()

    while True:
        guess = input("Promblem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time,2)

print(Fore.MAGENTA + f"--------------------------")
print(Fore.MAGENTA + Style.BRIGHT + f"Nice Work! You finished in {total_time} seconds :)")