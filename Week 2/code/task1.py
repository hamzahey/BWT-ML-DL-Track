import re

def get_user_input():
    # Prompt user for input
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    favorite_number = input("Enter your favorite number: ")

    # Store inputs in a dictionary
    user_info = {
        'name': name,
        'age': age,
        'email': email,
        'favorite_number': favorite_number
    }

    return user_info

def validate_email(email):
    # Validate email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_pattern, email):
        return True
    return False

def display_message(user_info):
    # Format and display the message
    message = f"Hello {user_info['name']}, you are {user_info['age']} years old, your email is {user_info['email']}, and your favorite number is {user_info['favorite_number']}."
    print(message)

def main():
    user_info = get_user_input()
    
    if validate_email(user_info['email']):
        display_message(user_info)
    else:
        print("Invalid email format. Please try again.")

if __name__ == "__main__":
    main()
