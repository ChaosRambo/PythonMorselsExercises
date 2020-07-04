import re


def count_words(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    wordlist = sentence.split(' ')
    words = {}
    for i in wordlist:
        i = i.lower()
        if i not in words:
            words[i] = 1
        elif i in words:
            words[i] += 1
    return words


if __name__ == '__main__':
    print(count_words("Oh what a day What a lovely day!"))
