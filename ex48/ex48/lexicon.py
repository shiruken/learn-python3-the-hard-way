LEXICON = {
    "north": "direction",
    "east": "direction",
    "south": "direction",
    "west": "direction",
    "go": "verb",
    "kill": "verb",
    "eat": "verb",
    "the": "stop",
    "in": "stop",
    "of": "stop",
    "bear": "noun",
    "princess": "noun"
}

def scan(command):
    words = command.split()
    output = []

    for word in words:
        try:
            output.append(('number', int(word)))
        except:
            word_type = LEXICON.get(word)

            if word_type is not None:
                output.append((word_type, word))
            else:
                output.append(('error', word))

    return output
