def wordCount(text: str) -> int:
    return len(text.split())


def getCharCount(text: str) -> dict[str,int]:
    characterCount: dict[str,int] = {}
    for c in text:
        if c in characterCount:
            characterCount[c] += 1
        else:
            characterCount[c] = 1
    return characterCount