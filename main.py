group_integer = []

user_input = int(input('insert an integer: '))

while user_input != 0:
    group_integer.append(user_input)
    user_input = int(input('insert an integer: '))

group_integer.sort()

for numbers in group_integer:
    print(numbers)