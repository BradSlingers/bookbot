import sys
from stats import get_num_words
from stats import get_num_chars
from stats import convert

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    the_path_to_book = sys.argv[1]
    the_contents = get_book_text(the_path_to_book)
    num_words = get_num_words(the_contents)
    num_chars = get_num_chars(the_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {the_path_to_book}...")
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