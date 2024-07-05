import os
import Employee
import pickle
import time

directory = input('Enter filepath: ')
lastNameHash = {}
idHash = {}

def buildDictionaries():
    for file in os.listdir(directory):
        if file.startswith('.'):
            continue
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                line = file.readline().strip()
                if line:
                    id, firstName, lastName, hireYear = line.split(',')
                    employee = Employee.Employee(id, firstName, lastName, hireYear)
                    lastNameHash[lastName] = employee
                    idHash[id] = employee


def serialize_employee_files():
    return


def print_directory_list():
    for file in os.listdir(directory):
        if file.startswith('.'):
            continue
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                line = file.readline().strip()
                if line:
                    id, firstName, lastName, hireYear = line.split(',')
                    employee = Employee.Employee(id, firstName, lastName, hireYear)
                    print(employee)


def deleteEmployee():
    employeeToDelete = input("enter employee id: ")
    filepath = os.path.join(directory, employeeToDelete + ".txt")

    try:
        os.remove(filepath)
        print(f"The employee {employeeToDelete} has been deleted successfully.")
    except FileNotFoundError:
        print(f"The employee {employeeToDelete} does not exist.")
    except PermissionError:
        print(f"Permission denied: {filepath}.")
    except Exception as e:
        print(f"An error occurred: {e}.")


def get_next_available_id():
    existing_ids = set()

    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            try:
                file_id = int(os.path.splitext(file)[0])
                existing_ids.add(file_id)
            except ValueError:
                pass

    next_id = 0
    while next_id in existing_ids:
        next_id += 1

    return next_id

def createEmployee():
    fname = input("enter a first name: ")
    lname = input("enter a last name: ")
    year = input('enter the year hired: ')

    employee = Employee.Employee(get_next_available_id(), fname, lname, year)
    save_new_entry(employee)
    return employee


def updateEmployee():
    runUpdate = True

    try:
        temp = input("Enter Id of who you want to update: ")
        employeeFile = find_employee(temp)
        if employeeFile is None:
            print("employee not found")
            return
        with open(employeeFile, 'r') as file:
            line = file.readline().strip()
            if line:
                id, firstName, lastName, hireYear = line.split(',')
                employee = Employee.Employee(id, firstName, lastName, hireYear)
    except FileNotFoundError:
        print(f"The employee {temp} does not exist.")
        runUpdate = False
    while runUpdate:
        hold = input(f'1 - Change First Name\n'
                     f'2 - Change Last Name\n'
                     f'3 - Change Hire Year\n'
                     f'4 - Quit\n')
        if hold == '1':
            employee.setfirstname(input('Enter new first name: '))
        if hold == '2':
            employee.setlastname(input('Enter new last name: '))
        if hold == '3':
            employee.sethireyear(input('Enter new hire year: '))
        if hold == '4':
            save_new_entry(employee)
            runUpdate = False


def find_employee(employee_id):
    filepath = os.path.join(directory, employee_id + ".txt")
    if os.path.exists(filepath):
        return filepath


def save_new_entry(employee):
    filepath = os.path.join(directory, str(employee.getid()) + ".txt")
    with open(filepath, 'w') as file:
        file.write(str(employee))


def print_employee(filePathToEmployee):
    with open(filePathToEmployee, 'r') as file:
        line = file.readline().strip()
        if line:
            id, firstName, lastName, hireYear = line.split(',')
            employee = Employee.Employee(id, firstName, lastName, hireYear)
            print(employee)


quitProgram = False


def main():
    global quitProgram
    global directory
    while not quitProgram:
        print("\n")
        print(f'1 - Print Directory List\n'
              f'2 - Change Database Directory\n'
              f'3 - Find Entry\n'
              f'4 - Delete Entry\n'
              f'5 - Create New entry\n'
              f'6 - Update Entry\n'
              f'7 - Quit\n')
        command = input('Enter command: ')
        if command == '1':
            print_directory_list()
        if command == '2':
            directory = input('Enter directory: ')
        if command == '3':
            employeeFile = find_employee(input('Enter Id of Employee: '))
            if employeeFile is None:
                print("employee not found")
                continue
            print_employee(employeeFile)
        if command == '4':
            deleteEmployee()
        if command == '5':
            createEmployee()
        if command == '6':
            updateEmployee()
        if command == '7':
            quitProgram = True


print("Building indexes...")
buildDictionaries();
print("Done\n")
main()
