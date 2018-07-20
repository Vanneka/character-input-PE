# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:18:36 2018

@author: VANESSA
"""
#TAB indented
#to import date time module
import datetime

#to collect users age
age = input("Enter your age: ")

#to store current year
currentDate= datetime.datetime.now()
currentYear= currentDate.year

#to get the birth year
birthYear= currentYear-int(age)

#for century age
centuryYear= birthYear + 100

#to display details
print("You are " + str(age) + " years old")
print ("You were born in the year " + str(birthYear))
print ("You will be 100 in the year " + str(centuryYear))

message ="You will be 100 in the year " + str(centuryYear) + "\n"

#to collect a new number to multiply the previous message by
newNumber = int(input("Enter a number between 1 and 10: "))
if int(newNumber) > 10:
    print(input("Please enter a number less than 10: "))

#to print out x number of text
print (newNumber * message)




