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

def add_contact(contact_list):
    name = input("\nType the name of the contact: ")
    phone = input("Type the phone of the contact: ")
    email = input("Type the email of the contact: ")

    contact = {
      "name": name,
      "phone": phone,
      "email": email,
      "favorite": False
    }

    contact_list.append(contact)

    print(f"\nContact {name} added successfully!")
    return
  
def update_contact(contact_list):
  contact_index = input("\nType the number of the contact you'd like to update: ")
  new_phone = input("\nType the new phone of the contact: ")
  new_email = input("Type the new email of the contact: ")

  adjusted_contact_index = int(contact_index) - 1
  
  if adjusted_contact_index >= 0 and adjusted_contact_index < len(contact_list):
    contact_list[adjusted_contact_index]["phone"] = new_phone
    contact_list[adjusted_contact_index]["email"] = new_email
    print("\nContact %s updated!" % contact_list[adjusted_contact_index]["name"])
  else:
    print("Invalid contact index.")
  return

def favorite_contact(contact_list):
  contact_index = input("\nType the number of the contact you'd like to favorite: ")
  adjusted_contact_index = int(contact_index) - 1

  contact_list[adjusted_contact_index]["favorite"] = True
  
  print("Contact %s checked as favorite" % contact_list[adjusted_contact_index]["name"])
  return