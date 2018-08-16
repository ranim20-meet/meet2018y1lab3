def name():
    name = input("What's your name? ")
    print("Hello there, " + name.capitalize() + "!")
    length = len(name)
    print("Your name is " + str(length) + " letters long!")
    print("The first letter of your name is " + (name[0]).upper() + " and the last letter is " + (name[(len(name)-1)].upper()))
    mood = input("How you doin'? ")
    mood = mood.lower()
    if mood == "good":
        print("I`m happy your`e having a good day!")
    elif mood == "bad":
        print("I hope you feel better!")

name()


# splicing claire #
string = "Hi there, mi name is Claire. Nice to meet you!"
string[21:28]
