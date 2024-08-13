def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letters_2(text)
    chars_sorted_list = dict_to_sorted(chars_dict)

    print(f"Report of {book_path}")
    print(f"{num_words} was found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print('End report')


def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters_2(text):
    letters = {}
    for w in text:
        lowered = w.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def sort_on(d):
    return d["num"]

def dict_to_sorted(num_chars_dict):
    sorted_list = []
    for c in num_chars_dict:
        sorted_list.append({"char": c, "num": num_chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()