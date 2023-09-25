firstname = input()
surname = input()
letter1 = len(firstname)
letter2 = len(surname)
username = surname[0], surname[1], surname[2], firstname[0],
print(username)
print("Enter username")
usernameguess = input()
if usernameguess == username:
    print("Correct!")
else:
    print("Incorrect!")

usernameguess = input()
while usernameguess != username:
    print("try again")
    usernameguess = input()

print("Please enter your password")
password = "chudbob"
passwordguess = input()
if passwordguess == password:
    print("Correct!")
else:
    print("INCORRECT!")
while passwordguess != password:
    print("try again")
    passwordguess = input()
