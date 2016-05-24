import sys
import re
import urllib

def main():

    dict = {
        "fr": "french",
        "en": "english",
        "de": "german",
        "es": "spanish",
        "ru": "russian",
        "pt": "portuguese",
        "it": "italian",
        "ja": "japanese",
        "zh": "chinese",
        "nl": "dutch",
        "pl": "polish",
        "da": "danish",
        "sv": "swedish",
        "fi": "finnish",
        "el": "greek",
        "cs": "czech",
        "ro": "romanian",
        "hu": "hungarian",
        "sk": "slovene",
        "lt": "lithuanian",
        "lv": "latvian",
        "et": "estonian",
        "mt": "maltese"
    }

    query = sys.argv[1]

    arguments = re.sub("[^\w]", " ",  query).split()

    try:
        fromTo = arguments[len(arguments) - 1]
    except IndexError:
        fromTo = "fren"

    if len(fromTo) != 4:
        fromTo = "fren"

    baseURL = "http://www.linguee.com/"
    try:
        firstLang = dict[fromTo[:2]]
    except KeyError:
        firstLang = "english"
    try:
        secondLang = dict[fromTo[2:]]
    except KeyError:
        secondLang = "english"

    languages = firstLang + "-" + secondLang
    query = query[:len(query) - 4]
    query = urllib.quote_plus(query)
    feedback = baseURL + languages + "/search?source=auto&query=" + query

    sys.stdout.write(feedback)
    sys.exit(0)

if __name__ == '__main__':
    main()