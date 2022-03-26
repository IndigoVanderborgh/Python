# For Loops I Core exercise 1
for i in range(0, 151):
    print(i)
# 2
for i in range(0,1000,5):
    print(i)
# 3
def counting_dojo():
    for i in range (1,101):
        if (i % 10) == 0:
            print ('Dojo')
        if (i % 5) == 0:
            print ('Coding')
counting_dojo()
# 4 done with help, will redo this one for practice by saturday!
minimum = 0
maximum = 500000
Oddtotal = 0
for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number
print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))
# 5
def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
count_down_four()  
# 6 
def flex_countdown(lowNum, highNum, mult):
    for i in range (lowNum, highNum):
        if i % mult == 0:
            print (i)
flex_countdown(2, 9, 3)

# % modular division takes the remainder of the number ie what the remainder is after division
# == comparison between left and reight value to see if they are the same. 