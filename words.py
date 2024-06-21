def print_upper_words(words):
    """Print each word as uppercased."""
    for word in words:
        print(word.upper())


def print_upper_e_words(words):
    """Print each word as uppercased, if starts with E or e."""
    for word in words:
        if word[0] == "e" or word[0] == "E":
            print(word.upper())

def print_accepted_upper_words(words, accepted_starting_letters):
    """Print each word as uppercased, if starts with the user's accepted letters"""
    for word in words:
        for accepted_letter in accepted_starting_letters:
            if word[0] == accepted_letter:
                print(word.upper())
                break
