# Consider two files that contain information about Employees and Departments in the
# following parameters: Employee (Name, EId, Salary, DID), Department (DID,
# DName, DLocation). Write a Python program to find the average salary of each department.

from Employee_Department.Employee import get_employees
from Employee_Department.Department import get_departments

def average_salary_by_department():
    employees = get_employees()
    departments = get_departments()

    dept_dict = {}
    for (did, dname, _) in departments:
        dept_dict[did] = dname

    salary_data = {}

    for (_, _, salary, did) in employees:
        if did not in salary_data:
            salary_data[did] = [0, 0]
        salary_data[did][0] += salary
        salary_data[did][1] += 1

    print("Average Salary by Department:") 
    for did, (total, count) in salary_data.items():
        avg = total / count 
        print(f"{dept_dict[did]}: {avg:.2f}")

average_salary_by_department()