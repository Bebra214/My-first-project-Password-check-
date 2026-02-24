pass1 = input("Enter your password: ")
pass2 = input("Enter your password again: ")

while pass1 != pass2:
    print("Password incorrect")
    pass1 = input("Enter your password: ")
    pass2 = input("Enter your password again: ")

print("Password correct")
print("Your can now access your account")
print(pass1, pass2)