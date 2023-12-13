import pytest
from unittest.mock import patch
from User import User
from main import UserInput, main

def test_initial_User():
    "function that test init a new user "
    user = User('John',23)
    assert user.username == 'John'
    assert user.age == 23

def test_UserGetStatus(capfd):
    "function that test the getstatus function make new user and test the output"
    user = User('John',23)
    User.GetStatus(user)
    out, err = capfd.readouterr()
    assert out == 'John, you are considered an adult!\n'

def test_UserInput():
    "function that test the userInput function with legal age"
    with patch('builtins.input', side_effect=['areen','25']):
        assert UserInput() == ('areen',25)

def test_UserIllegalInput():
    "function that test the userInput function with illegal then legal age "
    with patch('builtins.input', side_effect=['areen','-5','5']):
        assert UserInput() == ('areen',5)
