def create_contact(contacts):
    contact_name = input("Enter the name of the contact you want to add: ")
    contact_phone = input("Enter the phone number to add to the contact: ")
    contact_email = input("Enter the email to add to the contact: ")
    save_contact(contacts, contact_name, contact_phone, contact_email)

def save_contact(contacts, contact_name, contact_phone, contact_email):
    contact = {
        "name": contact_name,
        "phone": contact_phone,
        "email": contact_email,
        "favorite": False
    }
    contacts.append(contact)
    print(f"Contact {contact_name} has been added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts available.\n")
        return
    
    print("\nContact List:")
    for index, contact in enumerate(contacts, start=1):
        status = "★" if contact["favorite"] else " "
        print(f"{index}. [{status}] {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-" * 30)

def edit_contact(contacts, contact_index, new_contact_name, new_contact_phone, new_contact_email):
    try:
        adjusted_index = int(contact_index) - 1
        contacts[adjusted_index]["name"] = new_contact_name
        contacts[adjusted_index]["phone"] = new_contact_phone
        contacts[adjusted_index]["email"] = new_contact_email
        print(f"Contact {contact_index} updated to {new_contact_name}")
    except (ValueError, IndexError):
        print("Invalid contact index.")

def validate_index(contact_index, contacts):
    try:
        adjusted_index = int(contact_index) - 1
        return 0 <= adjusted_index < len(contacts)
    except ValueError:
        return False

def mark_favorite(contacts, contact_index):
    try:
        adjusted_index = int(contact_index) - 1
        contacts[adjusted_index]["favorite"] = True
        print(f"Contact {contact_index} marked as favorite.")
    except (ValueError, IndexError):
        print("Invalid contact index.")

def remove_favorite(contacts, contact_index):
    try:
        adjusted_index = int(contact_index) - 1
        contacts[adjusted_index]["favorite"] = False
        print(f"Contact {contact_index} removed from favorites.")
    except (ValueError, IndexError):
        print("Invalid contact index.")

def view_favorite_contacts(contacts):
    has_favorites = False

    print("\nFavorite Contacts List:")
    for index, contact in enumerate(contacts, start=1):
        if contact["favorite"]:
            print(f"{index}. {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print("-" * 30)  # Linha de separação
            has_favorites = True

def remove_contact(contacts, contact_index):
    try:
        adjusted_index = int(contact_index) - 1
        contact_name = contacts[adjusted_index]["name"]
        contacts.pop(adjusted_index)
        print(f"Contact {contact_name} removed.")
    except (ValueError, IndexError):
        print("Invalid contact index.")

def main():
    contacts = []
    while True:     
        print("\nContact Book:")
        print("1. Create Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Favorites")
        print("5. Remove Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_contact(contacts)
            
        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            view_contacts(contacts)
            contact_index = input("Enter the number of the contact you want to edit: ")
            if validate_index(contact_index, contacts):
                new_name = input("Enter the new name of the contact: ") 
                new_phone = input("Enter the new phone number of the contact: ")
                new_email = input("Enter the new email of the contact: ")
                edit_contact(contacts, contact_index, new_name, new_phone, new_email)
            else:
                print("Invalid contact index.")

        elif choice == "4":
            print("\nFavorites")
            print("1. Add contact to favorites")
            print("2. Remove contact from favorites")
            print("3. View favorites")
      
            option = input("Enter your desired option: ")

            if option == "1":
                view_contacts(contacts)
                contact_index = input("Enter the number of the contact you want to add to favorites: ")
                mark_favorite(contacts, contact_index)
              
            elif option == "2":
                view_favorite_contacts(contacts)
                contact_index = input("Enter the number of the contact you want to remove from favorites: ")
                remove_favorite(contacts, contact_index)
            
            elif option == "3":
                view_favorite_contacts(contacts)

        elif choice == "5":
            view_contacts(contacts)
            contact_index = input("Enter the number of the contact you want to remove: ")
            remove_contact(contacts, contact_index)
              
        elif choice == "6":
            break
    
    print("Program terminated")

if __name__ == "__main__":
    main()
