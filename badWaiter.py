#program acts like server for J. Timothy's Taverne in Plainville, CT
#James is an actual waiter there/friend/beer snob
#10/10 would reccomend
import time
total = [] #keeps track of total
print ('Hey guys. My name is James. I\'ll be your server.')
print('What would you like to drink today? Everything is $2.')
total.append(2)
a=str(input(''))
print('I\'ll be back with your ' + a + ' shortly')
time.sleep(5)
print('Here is your drink! I spilled a little on the way over. Sorry.')
print('Our kitchen was recently set on fire so we have limited menu options today')
#menu items. Long names.
print('Today we have the bucket of wings, french onion soup, BBQ baby back ribs, and teriyaki pineapple grilled salmon.')
print('Are you ready to order?')
b=str(input(''))
if b=='y' or b=='yes': #patron ready to order
    print('What would you like?')
    c=str(input(''))
    if c=='bucket of wings':
        total.append(40.95)
    elif c=='french onion soup':
        total.append(6.95)
    elif c=='teriyaki pineapple grilled salmon':
        total.append(21.95)
    elif c=='BBQ baby back ribs':
        total.append(24.95)
    print('I\'ll be back with your ' + c)
    time.sleep(5)
    print('Here is your food!')
    time.sleep(5)
    print('I want to go home so here is your check.')
    print('check:$' + str(sum(total)))
    time.sleep(5)
    print('Thanks! I\'ll be back with your receipt.')
    time.sleep(5)
    print('Here\'s your receipt. Y\'all come back now')
    
elif b=='n' or b=='no': #patron need more time
    print('I\'ll give you more time then.')
    time.sleep(10)
    print('Are you ready to order yet?')
    #repeat menu
    print('Today we have the bucket of wings, french onion soup, BBQ baby back ribs, and teriyaki pineapple grilled salmon.')
    d=str(input(''))
    if d=='y' or d=='yes':
        print('What would you like?')
        c=str(input(''))
        if c=='bucket of wings':
            total.append(40.95)
        elif c=='french onion soup':
            total.append(6.95)
        elif c=='teriyaki pineapple grilled salmon':
            total.append(21.95)
        elif c=='BBQ baby back ribs':
            total.append(24.95)
        print('I\'ll be back with your ' + c)
        time.sleep(5)
        print('Here is your food!')
        time.sleep(5)
        print('I want to go home so here is your check.')
        print('check:$' + str(sum(total)))
        time.sleep(5)
        print('Thanks! I\'ll be back with your receipt.')
        time.sleep(5)
        print('Here\'s your receipt. Y\'all come back now')
    elif d=='n' or d=='no': #patron need even more time and is abandoned
        print('I\'ll give you MORE time then.')
        print('James does not return. You are left to starve.')
        
