 #! python3
import re,pyperclip

phoneRegex=re.compile(r'((0*|\+91)?(\d{10}))')
emailRegex=re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''',re.VERBOSE)

text=pyperclip.paste()
extractedPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

allPhonenumbers=[]
for i in extractedPhone:
    allPhonenumbers.append(i[0])
#print(extractedPhone)
print('\n'.join(allPhonenumbers))
print('\n'.join(extractEmail))
    
