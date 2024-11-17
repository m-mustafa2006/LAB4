# Program to calculate salary based on years of service and qualification
years_of_service = int(input("Enter years of service: "))
qualification = input("Enter qualification (Masters/Bachelors): ").strip().capitalize()
if years_of_service >= 10:
    if qualification == "Masters":
        salary = 150000
    elif qualification == "Bachelors":
        salary = 100000
else:
    if qualification == "Masters":
        salary = 100000
    elif qualification == "Bachelors":
        salary = 70000
    else:
        salary = 0  # Optional, in case qualification is invalid
if salary > 0:
    print(f"Salary: {salary}")
else:
    print("Invalid qualification entered.")
