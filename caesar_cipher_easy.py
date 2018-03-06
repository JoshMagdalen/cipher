def translate_message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
               if num > ord('Z'):
                   num -= 26
               elif num < ord('A'):
                   num += 26
            elif symbol.islower():
               if num > ord('z'):
                   num -= 26
               elif num < ord('a'):
                   num += 26
            translated += chr(num)
        else:
             translated += symbol
    return translated

msg = translate_message("e", "Hello World", 2)
print(msg)



