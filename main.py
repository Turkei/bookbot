with open("books/frankenstein.txt") as f:

    # Import the book
    file_contents = f.read()
    
    # Calculate word count
    words = file_contents.split()
    print(f"\nThere are {len(words)} words in this book.")

    # Calculate letter count
    letter_count = {}

    for letter in file_contents.lower():
        if (letter in letter_count):
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    print()
    print(letter_count)