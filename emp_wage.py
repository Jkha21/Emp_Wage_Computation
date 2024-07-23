import random

def main():
    wage_per_hour = 20
    full_day = 8
    half_day = 4
    monthly_wage = 0
    
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
    print("")
    
    # Taking input from user for number of days
    total_no_of_days = int(input("Enter the number of days you were supposed to work (between 1 - 20): "))
    
    # Validate total_no_of_days
    if total_no_of_days < 1 or total_no_of_days > 20:
        print("Invalid number of days entered. Please enter a number between 1 and 20.")
        return
    
    total_hours = total_no_of_days * full_day
    counter = 0
    
    for i in range(1, total_no_of_days + 1):
        emp_check = random.randint(0, 2)
        
        if emp_check == 0:
            print(f"Employee is Present on day {i} and is working full time.")
            daily_wage = wage_per_hour * full_day
        elif emp_check == 1:
            print(f"Employee is Present but working part time on day {i}.")
            daily_wage = wage_per_hour * half_day
        else:
            print(f"Employee is Absent on day {i}.")
            daily_wage = 0
        
        print(f"The daily wage of Employee is : {daily_wage}")
        print("")
        
        monthly_wage += daily_wage
        counter += 1 if emp_check == 0 else 0
        
    print("")
    
    # Check conditions for additional bonuses
    if total_hours >= 100 or counter >= 20:
        print(f"The monthly wage of employee is : {monthly_wage}")
    else:
        print(f"The monthly wage of employee is : {monthly_wage}")

if __name__ == "__main__":
    main()
