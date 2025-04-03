fromHebrewToEnglish = {'t': 'א', 'c': 'ב', 'd': 'ג', 's': 'ד', 'v': 'ה', 'u': 'ו', 'z': 'ז', 'j': 'ח', 'y': 'ט',
                       'h': 'י', 'f': 'כ',
                       'k': 'ל', 'n': 'מ', 'b': 'נ', 'x': 'ס', 'g': 'ע', 'p': 'פ', 'm': 'צ', 'e': 'ק', 'r': 'ר',
                       'a': 'ש', ',': 'ת', 'q': '/', 'w': "'",
                       'i': 'ן', 'o': 'ם', 'l': 'ך', ';': 'ף', '.': 'ץ'}


def inputName(name):
    print("שלום לך ", end='')
    [print(changeLanguage(i), end='') for i in name if
     i.isalpha() and (ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'))]
    print()


explain = lambda: print(open(file='Explanation of the project.txt', mode='r', encoding='utf-8').read())


def changeLanguage(string):
    for i in string:
        for k, v in fromHebrewToEnglish.items():
            if i == k:
                string = string.replace(i, v)
    return string


def savedText(string):
    try:
        path = input("input path")
        with open(r"{}/translateText2.txt".format(path), 'w') as translateText2:
            translateText2.write(string)
    except:
        try:
            with open(r"C:\Users\This User\Downloads/translateText.txt", 'w') as translateText:
                translateText.write(string)
        except:
            print("oopss!")
