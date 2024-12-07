"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951578/homework
    
"""
import sys

# парсимо вхідні параметри
def parse_input(user_input:str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#add [ім'я] [номер телефону]
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name.lower() in contacts:
            return "Contact is already existing."
        contacts[name.lower()] = phone
        return "Contact added."
    else:
        return "Invalid command. Should be: add [ім'я] [номер телефону]"

#change [ім'я] [новий номер телефону]
def change_contact(args, contacts):
    if len(args) == 2:
        key = args[0].lower()
        if key not in contacts:
            return "Contact is not exist."    
        contacts[key] = args[1]
        return "Contact updated."
    else:
        return "Invalid command. Should be: change [ім'я] [номер телефону]"

#phone [ім'я]
def show_phone(args, contacts) -> str:
    if len(args) == 1:
        key = args[0].lower()
        if key not in contacts:
            return "Contact is not exist."    
        return contacts[key]
    else:
        return "Invalid command. Should be: phone [ім'я]"

#all
def show_all(args, contacts):
    if len(args)==0:
        all_contacts=""
        for key,val in contacts.items():
            all_contacts = all_contacts + key + ": " + val + "\n"
        return all_contacts
    else:
        return "Invalid command. Should be: all"

def main():
    contacts ={}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                sys.exit(0)
            case "hello":
                print("How can I help you?")
            case "all":
                print(show_all(args, contacts))
            #add [ім'я] [номер телефону]    
            case "add":
                print(add_contact(args, contacts))
            #change [ім'я] [новий номер телефону]
            case "change":
                print(change_contact(args, contacts))
            #phone [ім'я]
            case "phone":
                print(show_phone(args, contacts))
            case _:
                print("Invalid command.")

# program start
if __name__ =="__main__":
    main()