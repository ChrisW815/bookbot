with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()



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
                print(f"The '{letter}' character was found {dict[letter]} times")
        



    print("--- Bgin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    number_of_letters(file_contents)
    print("--- End report ---")
