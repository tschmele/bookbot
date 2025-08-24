import sys
from stats import get_word_count, get_char_count, sort_char_count

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")
    chars = get_char_count(book_text)
    chars = sort_char_count(chars)
    print_report(book_path, num_words, chars)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_report(path, count, chars):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count} total words")
    print(f"--------- Character Count -------")
    for c in chars:
        if not c["char"].isalpha():
            pass
        else:
            print(f"{c["char"]}: {c["num"]}")
    print(f"============= END ===============")

main()