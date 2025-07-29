"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()

def display_info(person, hobbies):
    print("\n--- Personal Information ---")
    print(f"Name    : {person[0]}")
    print(f"Age     : {person[1]}")
    print(f"City    : {person[2]}")
    print(f"Country : {person[3]}")
    print(f"Hobbies : {', '.join(hobbies) if hobbies else 'No hobbies added.'}")

def add_hobby(hobbies):
    hobby = input("Enter a new hobby: ")
    hobbies.append(hobby)
    print("Hobby added.")

def remove_hobby(hobbies):
    hobby = input("Enter a hobby to remove: ")
    if hobby in hobbies:
        hobbies.remove(hobby)
        print("Hobby removed.")
    else:
        print("Hobby not found.")

def update_age(person):
    try:
        new_age = int(input("Enter new age: "))
        person = (person[0], new_age, person[2], person[3])
        print("Age updated.")
    except ValueError:
        print("Invalid input. Age must be a number.")
    return person

def personal_info_manager():
    # Initial data
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    country = input("Enter your country: ")

    person = (name, age, city, country)
    hobbies = []

    while True:
        print("\n=== Personal Info Menu ===")
        print("1. Display information")
        print("2. Add a hobby")
        print("3. Remove a hobby")
        print("4. Update age")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_info(person, hobbies)
        elif choice == "2":
            add_hobby(hobbies)
        elif choice == "3":
            remove_hobby(hobbies)
        elif choice == "4":
            person = update_age(person)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
    