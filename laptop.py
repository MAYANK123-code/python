import pyperclip, re
mail= re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)

a = mail.search(r'biswasmayank0@gmailcom')
print(a.group())
