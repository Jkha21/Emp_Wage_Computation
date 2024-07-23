import random

def main():
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION =====")

    empCheck = random.randint(0, 1)
    if empCheck == 0:
        print("Employee is Present")
    else:
        print("Employee is Absent")

if __name__ == "__main__":
    main()