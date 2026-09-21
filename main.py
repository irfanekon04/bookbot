import sys
from stats import wordCount, getCharCount, charsDictToSortedList
def get_book_text(filepath:str) -> str:
    with open(filepath) as f:
        file_contents:str = f.read()
        return file_contents


def printReport(path: str,wordCount: int, sortedCharList: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")

    print("--------- Character Count -------")
    for char,count in sortedCharList:
        if not char.isalpha():
            continue
        print(f"{char}: {count}" )
    print("============= END ===============")

def main()-> None:
    if (len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookPath = sys.argv[1]
    file_contents :str = get_book_text(bookPath)
    wordsCount = wordCount(file_contents)
    sortedList = charsDictToSortedList(getCharCount(file_contents.lower()))
    printReport(bookPath,wordsCount,sortedList)

main()
