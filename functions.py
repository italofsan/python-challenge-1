def add_contact(contact_list):
    name = input("Type the name of the contact: ")
    phone = input("Type the phone of the contact: ")
    email = input("Type the email of the contact: ")

    contact = {
      "name": name,
      "phone": phone,
      "email": email,
      "favorite": False
    }

    contact_list.append(contact)
    print(f"Contact {name} added successfully!")
    return

def get_contact_list(contact_list):
  print("\nContact List")
  for index, contact in enumerate(contact_list, start=1):
    contact_name = contact["name"]
    phone = contact["phone"]
    email = contact["email"] 
    is_favorite = "✓" if contact["favorite"] else " "

    print(f"{index}. {contact_name} \
      Phone: {phone} \
      E-mail: {email} \
      Favorite: [{is_favorite}]")
    return