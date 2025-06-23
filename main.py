def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return str(book_contents)

from stats import word_count
from stats import letter_count
from stats import sorted_list
import sys    

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    letters = letter_count(book_text)
    sorted_letters = sorted_list(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    word_count(book_text)
    print("--------- Character Count -------")
    for entry in sorted_letters:
        if entry["char"].isalpha() == True:
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()

