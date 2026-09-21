from stats import wordCount, getCharCount
def get_book_text(filepath:str) -> str:
    with open(filepath) as f:
        file_contents:str = f.read()
        return file_contents


def main()-> None:
    file_contents :str = get_book_text("books/frankenstein.txt")
    wordsCount = wordCount(file_contents)
    print(f"Found {wordsCount} total words")
    print(getCharCount(file_contents.lower()))

main()