def find_max_min(numbers_list):
    """
    Takes a list of numbers and returns a tuple containing the maximum and minimum numbers.
    """
    max_num = max(numbers_list)
    min_num = min(numbers_list)
    return max_num, min_num

def main():
    """
    Main function to prompt the user to enter 5 numbers and find the max and min.
    """
    numbers = []
    print("Enter 5 numbers:")
    for i in range(5):
        num = float(input(f"Number {i+1}: "))
        numbers.append(num)

    max_num, min_num = find_max_min(numbers)
    print(f"The maximum number is: {max_num}")
    print(f"The minimum number is: {min_num}")

if __name__ == "__main__":
    main()
