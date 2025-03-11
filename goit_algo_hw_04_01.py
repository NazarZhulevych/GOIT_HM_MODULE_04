import pathlib

def total_salary(path):
    file_path = pathlib.Path(path)  # Use pathlib.Path instead of PurePath
    try:
        with file_path.open("r", encoding="utf-8") as fh:  # Open file safely
            records = []
            for line in fh:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Ignore empty lines
                    name, salary = line.split(",")  # Split into name and salary
                    records.append((name, float(salary)))  # Store as tuple
            
            total = sum(salary for _, salary in records)  # Compute total salary
            number_of_employees = len(records)
            if number_of_employees > 0:
                average_salary = total / number_of_employees  # Calculate average
                
            else:
                average_salary = 0
                print("Number of employees is less then 1")

            return total, average_salary
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except ValueError:
        print("Error: Invalid data format in file. Ensure each line follows 'Name,Salary' format.")
    except FileExistsError:
        print("File does not exist or unable to open")
# Use raw string (r"") or double backslashes (\\) for Windows paths

total, average = total_salary(r"C:\My_repo\GOIT_HM_MODULE_04\total_salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")