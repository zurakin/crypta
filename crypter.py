def crypt_letter(letter, code):
    return chr((ord(letter)+ord(code))%128)

def crypt_sequence(sequence, key):
    newsequence = ''
    for i in range(len(sequence)):
        newsequence += crypt_letter(sequence[i], key[i%len(key)])
    return newsequence


def crypt_file(file, key) :
    # try:
    with open(file, 'r') as text:
        content = text.read()
    with open(file, 'w') as text:
        content = key + content
        text.write(crypt_sequence(content, key))
    return 'file decryted succesfully'
    # except:
    #     return 'error while crypting'
