import pathlib

def get_cats_info(path):
    file_path = pathlib.Path(path)
    list_of_info = []

    try:
        with open(file_path, "r", encoding="UTF-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        id, name, age = line.split(",")  # Split values
                        record = {"id": id, "name": name, "age": age}  # Create dictionary
                        list_of_info.append(record)  # Append to list
                    except ValueError:
                        print(f"Invalid line format: {line}")  # Handle incorrect format

        return list_of_info  # Return list of dictionaries

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None  # Return None if the file is missing
    except ValueError:
        print("Not valid data in file")
    except FileExistsError:
        print("File does not exist or unable to open")

# Use raw string (r"") or double backslashes (\\) for Windows paths
print(get_cats_info(r"C:\My_repo\GOIT_HM_MODULE_04\cats_list.txt"))


