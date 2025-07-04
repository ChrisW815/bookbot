def number_of_words(contents):
    words = contents.split()
    print(f"Found {len(words)} total words")

def number_of_letters(text):
    lower_text = text.lower()
    dict = {}
    for letters in lower_text:
        if letters in dict:
            number_so_far = dict[letters]
            number_so_far += 1
            dict[letters] = number_so_far
        else:
            dict[letters] = 1

    letters = []
    letters = list(dict.keys())
    letters.sort()

    for letter in letters:
        if letter.isalpha():
            print(f"{letter}: {dict[letter]}")
