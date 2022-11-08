"""Changes words to upercase, only prints out words with specified start and end letter"""

def print_upper_words(words, must_start_with={"h", "y"}):
    for word in words:        
        word.upper()
        new_words = []
        if word[0] == must_start_with:
            new_words=[word]
    return new_words

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])