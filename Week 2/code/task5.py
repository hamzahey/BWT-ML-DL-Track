def main():
    # Step 1: Prompt the user to enter details of 3 students
    students_list = []
    for i in range(3):
        print(f"Enter details for student {i+1}:")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        students_list.append((name, age, grade))

    # Step 2: Convert the list of tuples into a dictionary
    students_dict = {student[0]: (student[1], student[2]) for student in students_list}

    # Step 3: Display the output
    print("\nStudent Details:")
    for name, details in students_dict.items():
        print(f"Name: {name}, Age: {details[0]}, Grade: {details[1]}")

if __name__ == "__main__":
    main()
