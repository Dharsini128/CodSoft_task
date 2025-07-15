contacts = []

# Add contact
def add_contact():
    print("\n➕ Add New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added!")

# View contacts
def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.")
        return
    print("\n📋 Contact List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} 📞 {c['phone']}")

# Search contact
def search_contact():
    key = input("\n🔍 Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if key in c["name"].lower() or key in c["phone"]:
            print(f"\n🔎 Found Contact:\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
            found = True
    if not found:
        print("❌ No contact found.")

# Update contact
def update_contact():
    view_contacts()
    try:
        index = int(input("\n✏️ Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave blank to keep existing value.")
            name = input(f"New Name ({contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"New Phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"New Email ({contacts[index]['email']}): ") or contacts[index]['email']
            address = input(f"New Address ({contacts[index]['address']}): ") or contacts[index]['address']
            contacts[index] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            print("✅ Contact updated!")
        else:
            print("⚠️ Invalid number.")
    except:
        print("⚠️ Invalid input.")

# Delete contact
def delete_contact():
    view_contacts()
    try:
        index = int(input("\n🗑️ Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"🗑️ Deleted contact: {removed['name']}")
        else:
            print("⚠️ Invalid number.")
    except:
        print("⚠️ Invalid input.")

# Main menu
def main():
    print("📘 Welcome to Contact Book!")
    while True:
        print("\n--- MENU ---")
        print("1. Add Contact ➕")
        print("2. View Contacts 📋")
        print("3. Search Contact 🔍")
        print("4. Update Contact ✏️")
        print("5. Delete Contact 🗑️")
        print("6. Exit 🚪")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice, try again.")

main()
