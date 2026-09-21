def wordCount(text: str) -> int:
    return len(text.split())


def sort_on(words : tuple[str,int]):
    return words[1]


def charsDictToSortedList(characterCount: dict[str,int]):
    charCount = []
    for keys in characterCount:
        count = characterCount[keys]
        charCount.append((keys,count))
    sortedCharCount = sorted(charCount,reverse=True,key=sort_on)
    return sortedCharCount


def getCharCount(text: str) -> dict[str,int]:
    characterCount: dict[str,int] = {}
    for c in text:
        if c in characterCount:
            characterCount[c] += 1
        else:
            characterCount[c] = 1
    return characterCount