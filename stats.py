def word_count(book):
    words = book.split()
    return len(words)

def num_characters(book):
    num_chars = {}
    no_dupes = book.lower()
    
    for char in no_dupes:
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1
    return num_chars