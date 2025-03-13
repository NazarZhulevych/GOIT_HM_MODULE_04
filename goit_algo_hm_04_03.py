from colorama import Fore, Style
import sys
from pathlib import Path

def print_folder_structure(directory: Path, indent: str = ""):
    if not directory.exists():
        print(f"Error: The directory '{directory}' does not exist.")
        return
    if directory.is_dir():
        print(Fore.BLUE + f"{indent}{directory.name}/" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"{indent}{directory.name}" + Style.RESET_ALL)
    
    for path in sorted(directory.iterdir()):
        if path.is_dir():
            print_folder_structure(path, indent + "    ")  
        else:
            print(Fore.GREEN + f"{indent}    {path.name}" + Style.RESET_ALL)


if len(sys.argv) < 2:
    print("Usage: python folder_structure.py <folder_path>")
else:
    folder_path = Path(sys.argv[1]).resolve()
    print_folder_structure(folder_path)