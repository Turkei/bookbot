with open("books/frankenstein.txt") as f:

    # Import the book
    file_contents = f.read()
    
    # Calculate word count
    words = file_contents.split()
    print(f"\nThere are {len(words)} words in this book.\n")

    # Calculate letter count
    letter_count = {}

    for letter in file_contents.lower():
        if (letter in letter_count):
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    letter_list = list(letter_count)
    letter_list.sort()

    for char in letter_list:
        if (char.isalpha()):
            print(f"The letter {char} appears {letter_count[char]} times.")