#program allows for practice of basic arithmetic with feedback
name = input('Hello. I am Math Bot. What is your name? :)')
print ('What do you want to practice today, %s? +, -, *, or /' %(input(name,)))
x = str(input(''))
from random import randint
#can edit numbers in range for more simplicity or difficulty
num1 = randint(0,50)
num2 = randint(0,10)

#allows for practice of addition
if x== '+':
    print ('Ok. What is ' + str(num1) + str('+') + str(num2))
    answer = num1 + num2
    addAnswer = int(input())
    if addAnswer == answer:
        print ('CORRECT')
    #provide feedback if too high or too low:
    elif addAnswer > answer:
        print ('too high!')
    elif addAnswer < answer:
        print ('too low!')
        
#allows for practice of subtraction
if x== '-':
    print ('Ok. What is ' + str(num1) + str('-') + str(num2))
    answer = num1 - num2
    subAnswer = int(input())
    if subAnswer == answer:
        print ('CORRECT')
    elif subAnswer > answer:
        print ('too high!')
    elif subAnswer < answer:
        print ('too low!')
        
#allows for practice of multiplication
if x== '*':
    print ('Ok. What is ' + str(num1) + str('*') + str(num2))
    answer = num1 * num2
    multAnswer = int(input())
    if multAnswer == answer:
        print ('CORRECT')
    elif multAnswer > answer:
        print ('too high!')
    elif multAnswer < answer:
        print ('too low!')
        
#allows for practice of division
if x== '/':
    print ('Ok. What is ' + str(num1) + str('/') + str(num2))
    answer = num1 / num2
    divAnswer = int(input())
    if divAnswer == answer:
        print ('CORRECT')
    elif divAnswer > answer:
        print ('too high!')
    elif divAnswer < answer:
        print ('too low!')
