from clase import HourlyEmployee,SalaryEmployee
employees = []
while True:
    print("Meniu:")
    print("1. Adăugare angajat")
    print("2. Afișare toți angajații")
    print("3. Ieșire")

    choice = input("Alege o opțiune: ")

    if choice == "1":
        name = input("Nume: ")
        phone = input("Telefon: ")
        bday = input("Data nașterii (format: dd/mm/yyyy): ")
        email = input("Email: ")
        position = input("Poziție: ")
        employee_type = input("Tip angajat (1 - Ore, 2 - Salariu): ")

        if employee_type == "1":
            hours_worked = float(input("Ore lucrate: "))
            hourly_rate = float(input("Tarif orar: "))
            new_employee = HourlyEmployee(name, phone, bday, email, position, hours_worked, hourly_rate)
        elif employee_type == "2":
            monthly_salary = float(input("Salariu lunar: "))
            new_employee = SalaryEmployee(name, phone, bday, email, position, monthly_salary)
        else:
            print("Opțiune invalidă. Reîncearcă.")

        employees.append(new_employee)
        print("Angajatul a fost adăugat cu succes!\n")

    elif choice == "2":
        for employee in employees:
            employee.display_info()
            print("\n")



    elif choice == "3":
        break

    else:
        print("Opțiune invalidă. Reîncearcă.")

print("Program încheiat.")

