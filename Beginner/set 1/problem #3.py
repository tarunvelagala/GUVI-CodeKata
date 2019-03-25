import re
try:
    str = input().lower()
    if re.findall(r'[aeiou]', str):
        print("vowel")
    elif re.findall(r'[^aeiou\$\d\s]', str):
        print("consonant")
    else:
        print("invalid")
except:
    print("invalid")
