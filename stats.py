def get_num_words(book_content):
    return len(book_content.split())

def get_char_count(book_content):
    words = book_content.lower().split()
    char_dict = {}
    for word in words:
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["value"]

def sort_char_counts(char_dict):
    # this uses Python's list comprehension to loop over each item
    # in the dictionary and add each item as a dictionary to the array
    dict_array = [{"char": key, "value": val} for key, val in char_dict.items()]
    
    # instead of defining a function for `key=` to call
    # we can define it as a lamda.
    dict_array.sort(reverse=True, key=lambda item: item["value"])
    return dict_array
