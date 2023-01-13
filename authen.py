'''
Authentication System
ระบบการยืนยันโดยใช้ชื่อและรหัสผ่าน
'''

#การลงทะเบียน สำหรับคนที่ยังไม่มีบัญชี
def registerUser():
    file_name = "account_database.txt"
    username_password = {}
    username = []
    password_confirm = []
    password = []
    print("Game Account Register")
    username.append(input("Username : "))
    password.append(input("Password : "))
    password_confirm.append(input("Confirm Password : "))
    while password != password_confirm:
        print("Wrong Confirm Password!! Please Try again")
        password.pop()
        password_confirm.pop()
        password.append(input("Password : "))
        password_confirm.append(input("Confirm Password : "))
    else:
        print("Register Successful!!")
        print("Your Username :", username[-1])
    username_password[username.pop()] = password.pop()

#ระบบการเขียนฐานข้อมูลเมือลงทะเบียนเสร็จสิ้น
    with open(file_name, "a+") as file:
        data = file.read()
        data = data
        for username, password in username_password.items():
            file.write(f"{username}, {password}\n")

#การลงชื่อเข้าใช้ สำหรับคนมีบัญชีแล้ว
def loginUser():
    print("Type 'exit' to exit to game.")
#ระบบการเช็คชื่อและรหัสผ่านจากฐานข้อมูล
    file_name = "account_database.txt"
    username_password = {}
    with open(file_name, "r+") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.replace("'", "")
            line = line.split(", ")
            username_password[line[0]] = line[1]
#การลงชื่อเข้าใช้ สำหรับคนมีบัญชีแล้ว โดยดึงจากฐานข้อมูลที่ได้ละเทียนไว้
    while True:
        login_username = input("Username : ")
        if login_username in username_password:
#           print("Welcome %s!" % login_username)
            print("Your are not", login_username+"?", "Type wrong password to retype username.")
            login_password = input("Password : ")
            if username_password[login_username] == login_password:
                print("Welcome %s!" % login_username, "to Game")
                break
            else:
                print("Wrong Password!!")
        elif login_username == 'exit':
            exit()
        else:
            print("Don't have account.")

registerUser()
loginUser()