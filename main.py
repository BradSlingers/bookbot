from stats import get_num_words
from stats import get_num_chars
from stats import convert

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    the_path_to_book = "books/frankenstein.txt"
    the_contents = get_book_text(the_path_to_book)
    num_words = get_num_words(the_contents)
    num_chars = get_num_chars(the_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_dicts = convert(num_chars)
    for entry in list_of_dicts:
        k = entry["char"]
        v = entry["num"]
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")



main()