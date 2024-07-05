import os
import Employee
import pickle
import time

directory = input('Enter filepath: ')
lastNameHash = {}
idHash = {}


def build_dictionaries():
    for file in os.listdir(directory):
        if file.startswith('.'):
            continue
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file2:
                line = file2.readline().strip()
                if line:
                    employee_id, first_name, last_name, hire_year = line.split(',')
                    employee = Employee.Employee(employee_id, first_name, last_name, hire_year)
                    lastNameHash[last_name] = employee
                    idHash[employee_id] = employee


def serialize_employee_files():
    return


def print_directory_list():
    for file in os.listdir(directory):
        if file.startswith('.'):
            continue
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file2:
                line = file2.readline().strip()
                if line:
                    employee_id, first_name, last_name, hire_year = line.split(',')
                    employee = Employee.Employee(employee_id, first_name, last_name, hire_year)
                    print(employee)


def delete_employee():
    employee_to_delete = input("enter employee id: ")
    filepath = os.path.join(directory, employee_to_delete + ".txt")

    try:
        os.remove(filepath)
        print(f"The employee {employee_to_delete} has been deleted successfully.")
    except FileNotFoundError:
        print(f"The employee {employee_to_delete} does not exist.")
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


def create_employee():
    first_name = input("enter a first name: ")
    last_name = input("enter a last name: ")
    year = input('enter the year hired: ')

    employee = Employee.Employee(get_next_available_id(), first_name, last_name, year)
    save_new_entry(employee)
    return employee


def update_employee():
    run_update = True

    temp = input("Enter Id of who you want to update: ")
    employee_file = find_employee(temp)
    try:
        if employee_file is None:
            print("employee not found")
            return
        with open(employee_file, 'r') as file:
            line = file.readline().strip()
            if line:
                employee_id, first_name, last_name, hire_year = line.split(',')
                employee = Employee.Employee(employee_id, first_name, last_name, hire_year)
    except FileNotFoundError:
        print(f"The employee {temp} does not exist.")
        run_update = False
    while run_update:
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
            run_update = False


def find_employee(employee_id):
    filepath = os.path.join(directory, employee_id + ".txt")
    if os.path.exists(filepath):
        return filepath


def save_new_entry(employee):
    filepath = os.path.join(directory, str(employee.getid()) + ".txt")
    with open(filepath, 'w') as file:
        file.write(str(employee))


def print_employee(file_path_to_employee):
    with open(file_path_to_employee, 'r') as file:
        line = file.readline().strip()
        if line:
            employee_id, first_name, last_name, hire_year = line.split(',')
            employee = Employee.Employee(employee_id, first_name, last_name, hire_year)
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
            employee_file = find_employee(input('Enter Id of Employee: '))
            if employee_file is None:
                print("employee not found")
                continue
            print_employee(employee_file)
        if command == '4':
            delete_employee()
        if command == '5':
            create_employee()
        if command == '6':
            update_employee()
        if command == '7':
            quitProgram = True


print("Building indexes...")
build_dictionaries()
print("Done\n")
main()
