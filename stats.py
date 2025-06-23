def word_count(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def letter_count(text):
    characters = {}
    for letter in text:
        if letter.lower() in characters:
            characters[letter.lower()] = characters[letter.lower()] + 1
        else:
            characters[letter.lower()] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_list(items):
    newlist = []
    for key, value in items.items():
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = value
        newlist.append(temp_dict)
    newlist.sort(reverse=True, key=sort_on)
    return newlist