def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return str(book_contents)

def word_count(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")
    

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count(book_text)

main()

