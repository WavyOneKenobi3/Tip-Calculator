#TIP Calculator
print("Welcome to the Tip Calculator")


def billing():
    user_input = float(input("how much is the total bill amount? "))    # ask for user input for bill amount
    
    tip_percentage = int(input("what percentage would you like to tip? 10%, 12%, 15%, 20%? "))              # what percentage of the tip to give? 10, 12, 15, 20
    
    split_bill = (input("would you like to split bill? Yes or No: ")).lower()               #will the total bill be split? 
    
    total_bill = float((tip_percentage * 100)/user_input) 
    
    if split_bill == "yes":
        num_people = int(input("How many people? "))   #number of people
        sum = total_bill / num_people           #total tip per person
        per_person = float(user_input + sum) 
        print(f"Bill total is: {user_input}. ")                       #total bill
        print(f"Total tip per person: {'%.2f' %sum}. ")                      #total tip per person (2 decimal places)
        print(f"Total bill plus tip amount: {per_person}. ")                                 #total bill + tip per person
    else:
        final_bill = total_bill + user_input           #total tip per person
        print(f"Total bill amount plus tip is: {final_bill}. ")                              
                
# rounded to 2 decimanls exp. 25.93 



billing()


