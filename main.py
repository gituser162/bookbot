import sys
from stats import *

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = args[1]
    text = get_book_text(book_path)
    characters = characters_counter(text)
    sorted_characters = sorted_dict(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_counter(text)} total words")
    print("---- Top 10 most common words ---")
    most_common_words(text)
    print("--------- Character Count -------")
    print_each_character(sorted_characters)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()