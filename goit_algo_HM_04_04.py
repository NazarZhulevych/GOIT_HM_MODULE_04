def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args 
    except ValueError:
        return "", []

def add_contact(args, contacts):
    try:
        if len(args) != 2:
            return "Error: Invalid input. Use: add <name> <phone>"
        name, phone = args
        if not phone.isdigit():
            return "Error: Phone number must be numeric."
        contacts[name] = phone
        return f"Contact {name} added."
    except Exception as e:
        return f"Unexpected error: {e}"

def change_number(args, contacts):
    try:
        if len(args) != 2:
            return "Error: Invalid input. Use: change <name> <new_phone>"
        name, phone = args
        if not phone.isdigit():
            return "Error: Phone number must be numeric."
        if name in contacts:
            contacts[name] = phone
            return f"Number for {name} updated."
        else:
            return f"User {name} not found."
    except Exception as e:
        return f"Unexpected error: {e}"

def find_phone(args, contacts):
    try:
        if len(args) != 1:
            return "Error: Invalid input. Use: phone <name>"
        name = args[0]
        return contacts.get(name, "Error: User not found.")
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    """Main function to handle user interactions."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ").strip()
            if not user_input:  
                print("Error: Please enter a command.")
                continue

            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Goodbye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "all":
                print(contacts if contacts else "No contacts found.")
            elif command == "change":
                print(change_number(args, contacts))
            elif command == "phone":
                print(find_phone(args, contacts))
            else:
                print("Error: Invalid command.")
        except KeyboardInterrupt:
            print("\nGoodbye!")  
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


