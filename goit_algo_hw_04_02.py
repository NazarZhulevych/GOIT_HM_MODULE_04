import pathlib

def get_cats_info(path):
    file_path = pathlib.Path(path)
    try:
        with open(file_path,"r",encoding= "UTF-8") as fh:
            records = {}
            list_of_info = []
            for line in fh:
                line = line.strip()
                if line:
                    id, name, age = line.split(",")
                    #records["id"] = {"name": str(name), "age": int(age)} 
                    records["id"] = {id} 
                    records["name"] = {str(name)} 
                    records["age"] = {int(age)} 
                    list_of_info.append(records)

        return list_of_info
    except ValueError:
        print("Not valid data in file")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except FileExistsError:
        print("File does not exist or unable to open")
    
    
        
print(get_cats_info("C:\My_repo\First_repo\cats_list.txt"))


