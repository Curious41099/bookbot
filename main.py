# # print("hello world")
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     number_of_words = get_count_words(text)
#     letters_dict = get_count_letters(text)

#     #  open and read the file
#     with open(book_path, 'r') as file:
#         text = file.read().lower()

#     word_count = len(text.split())

#     # Get character counts using the count_chars function
#     char_dict = count_chars(text)

#     # Print the report using the print_report function
#     print_report(char_dict,word_count)

# def get_book_text(path):
#     with open(path) as f:
#         file_contents = f.read()
#         return file_contents

# def get_count_words(text):
#     # the mistake i have done over here is that the input I have taken before is a contents in the file, but the real input here is a text from the book.
#     words = text.split()
#     return len(words)

# def get_count_letters(text):
#     letters = {}
#     for letter in text:
#         small_letter = letter.lower()
#         if small_letter in letters:
#             letters[small_letter] += 1
#         else:
#             letters[small_letter] = 1
#     return letters 

# # Counts each alphabet character in a given text and returns a dictionary with characters as keys and counts as values.
# def count_chars(text):
#     char_dict = {}
#     for char in text:
#         if char.isalpha():
#             if char in char_dict:
#                 char_dict[char] += 1
#             else:
#                 char_dict[char] = 1
#     return char_dict

# # Takes a dictionary of character counts and a total word count, 
# # sorts the characters based on their counts, and prints the report.
# def print_report(char_dict,word_count):
#     sorted_chars = sorted(char_dict.items(),key=lambda x: x[1], reverse=True)

#     print(f"Total words found: {word_count}")
#     for char,count in sorted_chars:
#         print(f"'{char}' character was found {count} times")






# main()

#initializing the main function.
def main():
    # Setting book path
    book_path = "books/frankenstein.txt"
    
    # Calling function to extract text from book
    text_content = extract_book_text(book_path)
    
    # Gathering count of words in book
    total_words = calculate_word_count(text_content)
    
    # Calculating frequency of each letter in book
    letter_frequency = calculate_letter_frequency(text_content)

    # Open and read the file
    with open(book_path, 'r') as book_file:
        text_content = book_file.read().lower()

    total_words = len(text_content.split())

    # Calculating frequency of each character in book
    char_frequency = calculate_character_frequency(text_content)

    # Displaying frequency report
    display_frequency_report(char_frequency, total_words)

# Function to read and return book contents
def extract_book_text(path):
    with open(path) as f:
        return f.read()

# Function to calculate number of words in a text
def calculate_word_count(text_content):
    words = text_content.split()
    return len(words)

# Function to calculate frequency of each letter in a text
def calculate_letter_frequency(text_content):
    letters_frequency = {}
    for letter in text_content:
        small_letter = letter.lower()
        if small_letter in letters_frequency:
            letters_frequency[small_letter] += 1
        else:
            letters_frequency[small_letter] = 1
    return letters_frequency 

# Function to calculate frequency of each character in a text
def calculate_character_frequency(text_content):
    char_frequency = {}
    for letter in text_content:
        if letter.isalpha():
            if letter in char_frequency:
                char_frequency[letter] += 1
            else:
                char_frequency[letter] = 1
    return char_frequency

# Function to generate and display frequency count report
def display_frequency_report(char_frequency, total_words):
    sorted_characters = sorted(char_frequency.items(),key=lambda x: x[1], reverse=True)

    print(f"Total words found: {total_words}")
    for char, count in sorted_characters:
        print(f"'{char}' character was found {count} times")

# Call main function
main()


