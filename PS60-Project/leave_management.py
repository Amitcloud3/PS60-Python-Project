from datetime import datetime

employees = {
    "E101": {
        "name": "Amit",
        "Casual": 12,
        "Sick": 10,
        "Earned": 15
    }
}

def apply_leave():
    emp_id = input("Enter Employee ID: ")
    if emp_id not in employees:
        print("Invalid Employee ID")
        return

    l_type = input("Enter Leave Type (Casual/Sick/Earned): ")
    if l_type not in ["Casual", "Sick", "Earned"]:
        print("Invalid Leave Type")
        return

    f_date = input("Enter From Date (YYYY-MM-DD): ")
    t_date = input("Enter To Date (YYYY-MM-DD): ")

    try:
        d1 = datetime.strptime(f_date, "%Y-%m-%d")
        d2 = datetime.strptime(t_date, "%Y-%m-%d")
    except:
        print("Invalid date format")
        return

    if d2 < d1:
        print("Invalid dates. To-date cannot be before from-date.")
        return

    days = (d2 - d1).days + 1
    bal = employees[emp_id][l_type]

    if days <= bal:
        employees[emp_id][l_type] = bal - days
        print("Leave approved:", days, "days", l_type, "| Balance", l_type + ":", employees[emp_id][l_type])
    else:
        print("Leave rejected. Requested:", days, "days | Available:", bal, "days")

def view_balance():
    emp_id = input("Enter Employee ID: ")
    if emp_id not in employees:
        print("Invalid Employee ID")
        return

    c = employees[emp_id]["Casual"]
    s = employees[emp_id]["Sick"]
    e = employees[emp_id]["Earned"]
    print("Casual:", c, "| Sick:", s, "| Earned:", e)

while True:
    print("\n1. Apply Leave")
    print("2. View Balance")
    print("3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        apply_leave()
    elif ch == "2":
        view_balance()
    elif ch == "3":
        break
    else:
        print("Wrong choice")