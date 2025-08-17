import sys
from stats import get_num_words, get_char_count, sort_char_counts

def get_book_text(file_path):
    # you can use with to open a file
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents


def main(book_path):
    file_content = get_book_text(book_path)
    num_words = get_num_words(file_content)
    char_counts = get_char_count(file_content)
    sorted_char_counts = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for d in sorted_char_counts:
        print(f"{d["char"]}: {d["value"]}")

# This special block only runs when you execute `python3 main.py`
# It will NOT run if you import this file into another Python script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from the command line...
    path_from_cli = sys.argv[1]

    # ...and pass it the your main function
    main(path_from_cli)