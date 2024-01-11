MORSE = { ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f",

"--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m",

"-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",

"..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z" }

text=input()
text=text.split()
for i in range(len(text)):
    for key in MORSE.keys():
        if text[i]==key:
            text[i]=text[i].replace(text[i],MORSE[key])
print(text)