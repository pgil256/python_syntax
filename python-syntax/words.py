"""Changes words to upercase, only prints out words with specified start and end letter"""

def print_upper_words(words, must_start_with):
    for word in words:       
        for letter in must_start_with:
            if word.startswith(letter):
                 print(word.upper())
                 break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])