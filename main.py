from functions import get_contact_list, add_contact, update_contact, favorite_contact

contact_list = []

while True:
    print("\nContact list menu")
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Edit a contact")
    print("4. Favorite a contact")
    print("5. Show all favorite contacts")
    print("6. Delete a contact")
    print("7. Exit")

    option = input("\nChoose your option: ")

    if option == "1":
        add_contact(contact_list)

    if option == "2":
        get_contact_list(contact_list)

    if option == "3":
        get_contact_list(contact_list)
        update_contact(contact_list)

    if option == "4":
        get_contact_list(contact_list)
        favorite_contact(contact_list)

    if option == "7":
        break

print("\nContact list closed!")