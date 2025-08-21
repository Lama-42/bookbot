def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count
from stats import num_characters


def main():
    book = get_book_text("books/frankenstein.txt")
    #print(book) 
    print(f"{word_count(book)} words found in the document")
    print(f"{num_characters(book)}")

main()
