import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

script_name = sys.argv[0]
book_path = sys.argv[1]



with open(book_path) as f:
    file_contents = f.read()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    number_of_words(file_contents)
    print("--------- Character Count -------")
    number_of_letters(file_contents)
    print("============= END ===============")



    



