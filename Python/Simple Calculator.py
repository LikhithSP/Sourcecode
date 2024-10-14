print('Welcome To Simple Calculator')
print("Please Select Your Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("0. Stop")
while True:
    operation = int(input('Enter your Choice(1/2/3/4/0)>> '))
    if operation > 4:
        print('Error 404')
        break
    elif operation < 0:
        print('Not Supported')
        break
    elif operation == 0:
        break
    numb1 = float(input("Enter Your First number>>  "))
    numb2 = float(input("Enter Your Second number>> "))

    if operation == 1:
        print(numb1+numb2)
    elif operation == 2:
        print(numb1-numb2)
    elif operation == 3:
        print(numb1*numb2)
    elif operation == 4:
        print(numb1/numb2)
    elif operation == 0:
        break
    else:
        print('Invalid Option. Please Try Again...')
