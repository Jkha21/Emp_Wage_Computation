import random

def main():
    wage_per_hour = 20
    full_day = 8
    half_day = 4
    total_no_of_days = 20
    
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
    print("")
    
    emp_check = random.randint(0, 2)
    
    if emp_check == 0:
        print("Employee is Present")
        daily_wage = wage_per_hour * full_day * total_no_of_days
        print(f"The daily wage of Employee is : {daily_wage}")
    elif emp_check == 1:
        print("Employee is Present but working part time")
        daily_wage = wage_per_hour * half_day * total_no_of_days
        print(f"The daily wage of Employee is : {daily_wage}")
    else:
        print("Employee is Absent")
        print("The daily wage of Employee is : 0")
    
    print("")

if __name__ == "__main__":
    main()
