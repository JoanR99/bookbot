def count_text_words(text):
    return len(text.split())

def count_text_chars(text):
    dictionary_count = {}
    
    for char in text:
        dictionary_count[char.lower()] = dictionary_count.get(char.lower(), 0) + 1
    
    return dictionary_count

def dictionary_to_list(dictionary):
    list = []
    
    for key, value in dictionary.items():
        list.append({"char": key, "qty": value})
        
    return list

def sort_dictionary_list(list):
    return sorted(list, key=lambda item: item["qty"], reverse=True)

def rank_char_count(dictionary):
    return sort_dictionary_list(dictionary_to_list(dictionary))