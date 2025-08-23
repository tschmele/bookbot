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