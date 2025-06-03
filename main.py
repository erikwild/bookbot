from stats import count_words, get_book_text
from stats import count_characters
from stats import sort_dicts
import sys

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book = sys.argv[1]
    print(f"Analyzing book found at {book}...")

    words = count_words(book)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    chars_dict = []
    text = get_book_text(book)

    print("--------- Character Count -------")
    chars_dict = count_characters(text)

    sorted_dicts = sort_dicts(chars_dict)
    for i in sorted_dicts:
        char = i['char']
        num = i['num']
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
main()
