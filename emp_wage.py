import random

def main():
    wage_per_hour = 20
    full_day = 8
    
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
    print("")
    
    emp_check = random.randint(0, 1)
    if emp_check == 0:
        print("Employee is Present")
        print(f"The daily wage of Employee is : {wage_per_hour * full_day}")
    else:
        print("Employee is Absent")
        print("The daily wage of Employee is : 0")
    
    print("")

if __name__ == "__main__":
    main()
