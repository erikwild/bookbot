def count_words(text):
        text = get_book_text(text)
        words = text.split()
        return len(words)

def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents

def count_characters(text):
    dict = {}
    low_text = text.lower()
    for c in low_text:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_dicts(chars_dict):
    list_of_dicts = []
    for c in chars_dict:
        list_of_dicts.append({
          "char": c,
          "num": chars_dict[c],
        })



    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
