def average_word_length(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()  # Tokenize the words
            total_length = sum(len(word) for word in words)  # Calculate total length
            average_length = total_length / len(words)  # Calculate average length
            return average_length
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except ZeroDivisionError:
        print("The file is empty. Cannot calculate average length.")
        return None

# Example usage:
file_path = 'dictionary.txt'
result = average_word_length(file_path)

if result is not None:
    print(f"The average length of words in the dictionary is: {result:.2f} characters.")