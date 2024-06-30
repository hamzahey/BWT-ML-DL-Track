# Library Management System

# Function to read data from a text file and print its contents
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
            return contents
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{filename}'.")

# Function to count the number of words in a given text
def count_words(text):
    words = text.split()
    return len(words)

# Function to write user input to a new file and handle exceptions
def write_to_file(filename, user_input):
    try:
        with open(filename, 'w') as file:
            file.write(user_input)
            print(f"Successfully wrote to the file '{filename}'.")
    except IOError:
        print(f"Error: An error occurred while writing to the file '{filename}'.")

# Main function to demonstrate file reading, word counting, and writing
def main():
    input_file = 'data.txt'
    output_file = 'output.txt'

    # Read and print the contents of 'data.txt'
    file_contents = read_file(input_file)
    
    if file_contents:
        # Count and print the number of words in 'data.txt'
        word_count = count_words(file_contents)
        print(f"The file '{input_file}' contains {word_count} words.")

    # Get user input and write it to 'output.txt'
    user_input = input("Enter text to write to output.txt: ")
    write_to_file(output_file, user_input)

# Entry point of the program
if __name__ == "__main__":
    read_file('output.txt')
