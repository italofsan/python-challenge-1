def add_contact(contact_list, contact_name):
    contact = {"name": contact_name, "favorite": False}
    contact_list.append(contact)
    print(f"Contact {contact_name} added successfully!")
    return

def get_contact_list(contact_list):
  print("\nContact List")
  for index, contact in enumerate(contact_list, start=1):
    contact_name = contact["name"]
    print(f"{index}. {contact_name}")
    return