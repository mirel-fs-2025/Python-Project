import projectFunctions

name = input("input your first name")
projectFunctions.inputName(name)
projectFunctions.explain()
text = input("input text to do the code")
text = projectFunctions.changeLanguage(text)
print(text)
projectFunctions.savedText(text)
