import random

def generate_numbers():
    return random.sample(range(1,10),4)

def present_problem(numbers):
    problem = " ".join(map(str,numbers))
    return problem

def check_answer(answer):
    if eval(answer) == 24:
        return True
    else:
        return False

def play_game():
    numbers = generate_numbers()
    problem = present_problem(numbers)
    print("Use the numbers {} to make 24".format(problem))
    answer = input("Enter your answer: ")
    while not check_answer(answer):
        print("Incorrect, try again")
        answer = input("Enter your answer: ")
    print("Correct!")

play_game()