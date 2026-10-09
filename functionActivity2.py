# problem #1 
# create a function that will take in 2 inputs and compare them.
# your inputs should be numbers.
# the funnction should compare if the first input is less than the second input.
# if it is less than the second inpunt it should orint true. If it is not, it should print false 




def compareval():
    numA= input()
    numB= input()
    print(numA <= numB)


    compareval()

    # problem 2
    # create a functuion that will compare if a student has made honor roll.
    # the student should be able to input 2 pieces of data
    # the first should ne their garde and the second should be the number of days they have been absent
    if the students garde is above a 90 and the numberof absense is less than 5, the program should print true otherwise it should print false.

def honor_roll(grade, absences):
    if grade > 90 and absences < 5:
        print(True)
    else:
        print(False)

grade = float(input("Enter your grade: "))
absences = int(input("Enter the number of days absent: "))

honor_roll(grade, absences)

