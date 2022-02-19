#!/usr/bin/env python3
# Python 3.9.6
import random

"""
This PasswordGenerator Class will generate password
It take number of lettere, number and symbol 
Based on these input it will return password
"""


class PasswordGenerator:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def __init__(self, nmr_letter, nmr_number, nmr_symbol):
        self.nmr_letter = int(nmr_letter)
        self.nmr_number = int(nmr_number)
        self.nmr_symbol = int(nmr_symbol)
        self.total_pass_chrs = int(nmr_letter+nmr_number+nmr_symbol)

    def totalLetter(self):
        """ Generate total letters based on user input """
        letter = ""
        for chr in range(0, self.total_pass_chrs):
            if len(letter) != self.nmr_letter:
                letter += random.choice(self.letters)
        return letter

    def totalNumber(self):
        """ Generate total number based on user input """
        number = ""
        for chr in range(0, self.total_pass_chrs):
            if len(number) != self.nmr_number:
                number += random.choice(self.numbers)
        return number

    def totalSymbol(self):
        """ Generate total symbol based on user input """
        symbol = ""
        for chr in range(0, self.total_pass_chrs):
            if len(symbol) != self.nmr_symbol:
                symbol += random.choice(self.symbols)
        return symbol

    # add all the generated chars
    def combineAllCharacters(self):
        return self.totalSymbol() + self.totalNumber() + self.totalLetter()

    # mix all the characters
    def createPassword(self):
        password = []
        for p in self.combineAllCharacters():
            password.append(p)
        password = random.sample(password, len(password))
        return "".join(password)


# Letters :5
# number: 4
# symbol: 3
password = PasswordGenerator(5, 4, 3)
print(password.createPassword())
