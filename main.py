import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count
from stats import num_characters
from stats import convert_sort



def main():
    book_path = (path_to_file)
    book = get_book_text(book_path)
    stats = num_characters(book)
    sorted_stats = convert_sort(stats)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")
    for item in sorted_stats:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()








    #print(f"{word_count(book)} words found in the document")
    #print(f"{num_characters(book)}")
    #print(f"{convert_sort(stats)}")

