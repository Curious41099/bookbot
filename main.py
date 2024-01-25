# print("hello world")
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_count_words(text)
    letters_dict = get_count_letters(text)
    sorted_chars_list = char_dict_to_sorted_list(letters_dict)


    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print()

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")


    




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

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list







main()


