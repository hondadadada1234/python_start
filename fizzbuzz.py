i = 1

while i <= 100:
    if(i % 15 == 0):
        print('fizzBuzz')
    elif(i % 5 == 0):
        print('fizz')
    elif(i % 3 == 0):
        print('fizzBuzz')
    else:
        print(i)

    i = i + 1
