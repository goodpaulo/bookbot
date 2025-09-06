from stats import get_num_words
from stats import get_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

main()

get_num_words(get_book_text("books/frankenstein.txt"))

character_count = get_num_characters(get_book_text("books/frankenstein.txt"))

print(character_count)