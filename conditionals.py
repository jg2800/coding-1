# conditional if/else logic- these are keywords that instruct your 
# programe to do specific instructions based on specific data.
# or conditions
# conditions syntax ( how it is written )

bill_amount = int(input(" please toe in a bill tender ( 1,5,10)
# if usally indicates that something is a possible option
if bill_amount ==1:
    print("here are 4 quaters")
    # else always your last option
    else:
      prnit("Sorry that type of bill is not accepted")
      # elif allows us to indicate that there are more possible options
      # you can have as many elif as you want
        bill_amount==5
        print("here are 40 quarters")
        elif bill_amount ==10
         print("here are 40 0quarters")

         elif bill_amount==20 
         print("sorry we do not accepts 20s. Please enter an accepted amount")

   elif bill_amount==50
   print("sorry we do not accept 50s. Please enter an accepted amount.")


   elis n=bill_amount==100
      print("sorry we do not accepts 100s.please enter an accepted amount")
      # else is always your last options
      else:
        print("sorry that type of bill is not accepted")

       # create an calculator funxtions that uses if/else logic to allow the user
       # to change or select different arithmethic operators.
       # explames: an input where if teh user enter 1 it will do 
       # additions , 2 will do subtraction 
       # 3 will do multiplication and 4 divison

       def calculator():
    print("=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = int(input("Select an operator (1-4): "))

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = num1 + num2
        print("Result:", result)

    elif choice == 2:
        result = num1 - num2
        print("Result:", result)

    elif choice == 3:
        result = num1 * num2
        print("Result:", result)

    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Cannot divide by zero!")

    else:
        print("Invalid choice! Please select a number from 1 to 4.")


        # using the calulator functions from the calulator.py file
        # create a main calulator functions that uses if/else logic to
        # allows the user to select different arithmetic  

        def maincalulator():
         # take in a user selection as a number
         selection= input()

         if selection == 1:
         calculate_add()
        elif selection == 2
         if selection == 3
         calculate_subtract()
         elif selection == 4
          calculate_multiply 
          calculate_divsion
          
        