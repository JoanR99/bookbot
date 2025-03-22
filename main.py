import sys
from stats import count_text_words, count_text_chars, rank_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_text_words(text)} total words")
    print("--------- Character Count -------")
    char_count_dictionary = count_text_chars(text)
    char_count_ranked_list = rank_char_count(char_count_dictionary)
    for item in char_count_ranked_list:
        key = item["char"]
        value = item["qty"]
        if(key.isalpha()):
            print(f"{key}: {value}")
    print("============= END ===============")
    
main()