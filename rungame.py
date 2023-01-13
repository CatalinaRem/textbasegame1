import authen
import roshambo
import game24

print("Welcome to Textbase Games")
print("Plese Login or Register to Games")
choose = input("1 for Login\n2 for Register\nType number for choose : ")
while True:
    if choose in '1':
        authen.loginUser()
        break
    elif choose in '2':
        authen.registerUser()
        break
    elif choose in 'exit':
        exit()
    else:
        print("Error Plese Try Again")

while True:
    choose = input("Program have 2 games\n1 for Rock paper scissors \n2 for 24 Game \n0 or exit for Exit \nType number for choose games : ")
    if choose in '0':
        exit()
    elif choose in '1':
        roshambo.play_game()
    elif choose is '2':
        game24.play_game()
    elif choose is 'exit':
        print("Bye!!")
        exit()
    else:
        print("Error!! please Try again")
