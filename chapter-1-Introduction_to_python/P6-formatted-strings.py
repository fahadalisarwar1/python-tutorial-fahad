if __name__ == "__main__":
    name = "Fahad"
    age = 100
    print(f"The user name is {name}")
    print("hi " + name)
    print("Your age is " + str(age))
    print(f"your name is {name} and your age is {age}") # new method in python 3 more neat

    print("hi {} and your age is {}".format(name, 44)) # old method in python 2
    print("hi {0} and your age is {1}".format(name, 44)) # old method in python 2
    print("hi {1} and your age is {0}".format(name, 44)) # old method in python 2

    # this is an error
    # print("hi {0} and your age is {1}".format(name="sarwar", age=34)) # old method in python 2
    print("hi {name} and your age is {age}".format(name="sawrar", age=434)) # old method in python 2