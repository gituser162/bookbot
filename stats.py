def words_counter(text_to_count):
    words = text_to_count.split()
    return len(words)

def characters_counter(text_to_count):
    text_to_lower = text_to_count.lower()
    all_chars_dict = {}
    for char in text_to_lower:
        if not char.isalpha():
            continue
        if char in all_chars_dict:
            all_chars_dict[char] += 1
        else:
            all_chars_dict[char] = 1
    return all_chars_dict

def sorted_dict(dict_to_sort):
    array_of_sorted_dict = dict(sorted(dict_to_sort.items()))
    return array_of_sorted_dict

def print_each_character(characters):
    for character in characters:
        print(f"{character}: {characters[character]}")