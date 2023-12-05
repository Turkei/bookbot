with open("books/frankenstein.txt") as f:

    # Import the book
    file_contents = f.read()
    print(file_contents)

    # Calculate word count
    words = file_contents.split()
    print(f"\nThere are {len(words)} words in this book.")