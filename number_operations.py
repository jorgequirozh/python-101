def main():
    usernumber=input('Enter a number\n')
    selection=input('Select an operation:\n 1: Square\n 2: Seconds to minutes\n 3: Add two\n')
    while selection != str(1) and selection != str(2) and selection != str(3):
        print('Invalid choice, try again')
        selection=input('Select an operation:\n 1: Square\n 2: Seconds to minutes\n')
    if int(selection) == 1:
        print(usernumber, ' squared is: ',square(usernumber))
    elif int(selection) == 2:
        print(usernumber, ' seconds equals ', calculate_minutes(usernumber), 'minutes' )
    elif int(selection) == 3:
        print(usernumber, ' plus 2 equals ', add_two(float(usernumber)))

def calculate_minutes(seconds):
    minutes = int(seconds) / 60
    return minutes

def square(num):
    numSquared = int(num) * int(num)
    return numSquared

add_two = lambda x: x + 2

if __name__ == '__main__':
    main()
