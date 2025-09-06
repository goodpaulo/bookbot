def get_num_words(book_text):
    number_of_words = len(book_text.split())
    print(f"{number_of_words} words found in the document")

def get_num_characters(book_text):
    book_dict = {}
    for character in book_text:
        character = character.lower()
        if character in book_dict:
            book_dict[character] += 1
        else:
            book_dict[character] = 1
    return book_dict