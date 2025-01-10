def main():
    BOOK_PATH = "books/frankenstein.txt"
    with open(BOOK_PATH) as f:
        file_contents = f.read()
        word_count = get_num_words(file_contents)
        char_dict = count_chars(file_contents)

        make_report(word_count, char_dict)
        

def get_num_words(text):
    return len(text.split())

def count_chars(text):
    ret = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in ret.keys():
            ret[lowered_char] += 1
        else:
            ret[lowered_char] = 1

    return ret

def make_report(word_count, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for key in char_dict.keys():
        print(f"The '{key}' character was found {char_dict[key]} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
