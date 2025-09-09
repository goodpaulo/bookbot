def get_num_words(book_text):
    number_of_words = len(book_text.split())
    print(f"Found {number_of_words} total words")

def get_num_characters(book_text):
    book_dict = {}
    for character in book_text:
        character = character.lower()
        if character in book_dict:
            book_dict[character] += 1
        else:
            book_dict[character] = 1
    return book_dict

def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    dict_list = []
    for key, value in dictionary.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key = sort_on)
    return dict_list