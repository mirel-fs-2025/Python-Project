
# A dictionary where the key is a letter in Hebrew and the value is a letter in English
fromHebrewToEnglish={'t' :'א' ,'c' :'ב' ,'d' :'ג' ,'s' :'ד' ,'v' :'ה' ,'u' :'ו' ,'z' :'ז' ,'j' :'ח' ,'y' :'ט' ,'h' :'י' ,'f' :'כ',
                     'k' :'ל' ,'n' :'מ' ,'b' :'נ' ,'x' :'ס' ,'g' :'ע' ,'p' :'פ' ,'m' :'צ' ,'e' :'ק' ,'r' :'ר' ,'a' :'ש' ,',' :'ת' ,'q' :'/' ,'w' :"'",
                     'i' :'ן' ,'o' :'ם' ,'l' :'ך' ,';' :'ף' ,'.' :'ץ'}


# A function that prints a login message to the user.
# if the information is entered when the keyboard is in English mode
# it uses the conversion function and prints a string with his name
# so that he notices that the keyboard is in English
# otherwise prints a hello message
def inputName(name):
    print("שלום לך ",end='')
    [print(changeLanguage(i),end='') for i in name if i.isalpha() and (ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'))]
    print()


# The lambda function prints the document with an explanation of the project
explain=lambda:print(open(file='Explanation of the project.txt',mode='r',encoding='utf-8').read())


# A function that changes texts from Hebrew to English
def changeLanguage(string):
    for i in string:
        for k ,v in fromHebrewToEnglish.items():
            if i==k:
                string = string.replace(i, v)
    return string

# A function that saves the document in the selected path
def savedText(string):
    try:
        path=input("input path")
        with open(r"{}/translateText2.txt".format(path), 'w') as translateText2:
            translateText2.write(string)
    except:
           try:
               #ע"מ שירוץ לתוך ההורדות במחשב שונה צריך להחליף ידנית את \This User\ לשם משתמש בו אתה פתוח
               with open(r"C:\Users\This User\Downloads/translateText.txt", 'w') as translateText:
                translateText.write(string)
           except:
               print("oopss!")

