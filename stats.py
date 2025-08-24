def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    source = text.lower()
    chars = {}
    for c in source:
        try:
            chars[c] += 1
        except KeyError:
            chars[c] = 1
        except Exception as e:
            print(e)
    return chars

def sort_on(items):
    return items["num"]

def sort_char_count(chars):
    sorted = []
    for c in chars:
        sorted.append({"char": c, "num": chars[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
