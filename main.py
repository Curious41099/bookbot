# print("hello world")
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_count_words(text)
    letters_dict = get_count_letters(text)

    #  open and read the file
    with open(book_path, 'r') as file:
        text = file.read().lower()

    word_count = len(text.split())

    # Get character counts using the count_chars function
    char_dict = count_chars(text)

    # Print the report using the print_report function
    print_report(char_dict,word_count)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_count_words(text):
    # the mistake i have done over here is that the input I have taken before is a contents in the file, but the real input here is a text from the book.
    words = text.split()
    return len(words)

def get_count_letters(text):
    letters = {}
    for letter in text:
        small_letter = letter.lower()
        if small_letter in letters:
            letters[small_letter] += 1
        else:
            letters[small_letter] = 1
    return letters 

# Counts each alphabet character in a given text and returns a dictionary with characters as keys and counts as values.
def count_chars(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

# Takes a dictionary of character counts and a total word count, 
# sorts the characters based on their counts, and prints the report.
def print_report(char_dict,word_count):
    sorted_chars = sorted(char_dict.items(),key=lambda x: x[1], reverse=True)

    print(f"Total words found: {word_count}")
    for char,count in sorted_chars:
        print(f"'{char}' character was found {count} times")






main()


