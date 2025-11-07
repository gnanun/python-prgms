print("Contact book")
contacts = {}
while True:
    print("\n1. Add a new contact\n2. Search for a contact\n3. Exit the contact book")
    command =int(input("Enter command (1-3): "))
    if command == 1:
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"Contact {name} added.")
    elif command == 2:
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"\n{name}: {contacts[name]}")
        else:
            print(f"\nContact {name} not found.")
    elif command ==3:
        print("Exiting contact book.\n")
        break
    else:
        print("Unknown command. Please try again.")
        