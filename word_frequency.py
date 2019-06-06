STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    # Use with open to read the file
    with open(file) as source_file:
          source_file = source_file.read()
          source_file = clean_text(source_file)
          print(source_file)

    

def clean_text(text):
    """
    Remove punctuation from string
    """
    text = text.replace(",", "").replace("!", "").replace(".", "").replace("`", "")
    text = text.lower()
    text = text.split(" ")
    for word in list(text):
        if word in STOP_WORDS:
            print(word)
            text.remove(word)
                    
    return text



def count_word_freq(text):
    """
    Count how many times word have been used
    """
    pass







if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
