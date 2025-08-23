from stats import get_word_count, get_char_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")
    chars = get_char_count(book_text)
    print(f"the following letters have been found:\n{chars}")

main()