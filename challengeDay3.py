# 1
def age_func():
    age = (input("How old are you? "))
    if "." in age:
        print("Invalid number, please try again.\n")
        age_func()
    else:
        future = 2018+(100-(int(age)))
        print("You will be 100 years old in year " + str(future) + ".")
        
#age_func()

def dividable():
    num = int(input("Choose a number: "))
    if num %2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
    if num %7 == 0:
        print("Your number is divisible by 7.")
    else:
        print("Your number is not divisible by 7.")
