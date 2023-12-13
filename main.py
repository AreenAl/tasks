# This is a sample Python script.
import testing
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from User import User
import logging

def UserInput():
    '''
    function that get inputs from the user and check if the age is legal if not it ask for another number
    '''
    Name = input("Please enter your name?\n")
    temp = 1
    while temp:
        Age = input("Please enter your age?\n")
        if Age.isdigit():
            if (int(Age) > 0):
                temp = 0
                Age = int(Age)
                return Name,Age
        else:
            logging.error(' %s raised an error, write a legal age please!', Age)

def main():
    '''
    main function that get a list of users and print the status of each user
    '''
    list=[]
    status="0"
    while status!="1":
            Name,Age=UserInput()
            user=User(Name,Age)
            list.append(user)
            status=(input("if you want to stop the operation press 1 please\n"))

    #printing the list of users
    line=("The users status!!")
    print(line.center(100))
    for user in list:
        user.GetStatus()

if __name__ == '__main__':
    main()
    testing()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
