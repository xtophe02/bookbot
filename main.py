import re
from collections import Counter

# Define the path to the file
path_to_file = "books/frankenstein.txt"


def extract_alpha_chars(input_string):
    """
    Extracts only alphabetic characters (a-z, A-Z) from the input string.
    """
    return "".join(re.findall(r"[a-zA-Z]", input_string))


def count_words(text):
    """
    Counts the number of words in the given text.
    """
    return len(text.split())


def count_chars(text):
    """
    Counts the frequency of each alphabetic character in the text (case insensitive).
    Returns a dictionary sorted by frequency in descending order.
    """
    new_text = extract_alpha_chars(text)
    char_counts = Counter(new_text.lower())  # Use Counter for simplicity
    return dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))


def read_file(path):
    """
    Reads the content of a file and returns it as a string.
    Includes error handling for file operations.
    """
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except IOError as e:
        print(f"Error: Unable to read the file '{path}'. Details: {e}")
        return None


def print_report(file_path, word_count, char_counts):
    """
    Prints a report summarizing word count and character frequency in the document.
    """
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document.")
    for char, count in char_counts.items():
        print(f"The character '{char}' was found {count} times.")
    print("--- End report ---")


def main():
    """
    Main function to process the file and generate the report.
    """
    text = read_file(path_to_file)
    if text is not None:  # Proceed only if the file was read successfully
        word_count = count_words(text)
        char_counts = count_chars(text)
        print_report(path_to_file, word_count, char_counts)


if __name__ == "__main__":
    main()
