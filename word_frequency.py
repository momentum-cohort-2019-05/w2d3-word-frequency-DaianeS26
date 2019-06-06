STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]

#function is called in the end. It works on both files. This is why file is called first.
def print_word_freq(file):
    with open(file) as source_file:
        #create a variable
        text_file = source_file.read()
        # print(text_file)

        text_file_rem_punc= text_file.replace(",", "").replace("!", "").replace(".", "").replace("`", "").replace("--","")
        # print(text_file_rem_punc)
        text_lower_space = text_file_rem_punc.lower().split(" ")
        # print(text_lower_space)

    #loop through list and remove bad words
    for word in list (text_lower_space):
        if word in STOP_WORDS:
            text_lower_space.remove(word)
            
    # print(text_lower_space)

    #loop through list and create a dictionary
    dict_text ={}
    for word in text_lower_space:
        if word not in dict_text.keys():
            dict_text[word] = 1
        else:
            dict_text[word] +=1

    sorted_words= sorted(dict_text.items(), key=lambda x: x[1], reverse=True)
    for word, frequency in sorted_words[0:10]:
        print(word, "|", frequency, "*" * frequency)

#End of code I worked on. 
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
