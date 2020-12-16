import random

min = int(input('Enter the minumum value of the die: '))
max = int(input('Enter the maximum value of the die: '))

again = True

while again:
    print(random.randint(min, max))

    another_roll = input('Do you want to rool again?(yes): ') 

    if another_roll.lower() == 'yes':
        continue

    else:
        break