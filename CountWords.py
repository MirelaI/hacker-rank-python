import sys

def count_words(filename, word):
    file_handle = open(filename, 'r')
    counter = 0
    for line in file_handle:
        counter += line.split(" ").count(word)

    return counter

def main(argv):
    filename = None
    word = None
    try:
        filename = argv[0]
    except:
        print("Error when reading the filename input")
        raise

    try:
        word = argv[1]
    except:
        print("Error when reading the name input")
        raise

    no_of_occurences = count_words(filename, word)
    print("Word '{}' in filename {} found {} times").format(word, filename, no_of_occurences)

if __name__ == "__main__":
    main(sys.argv[1:])


