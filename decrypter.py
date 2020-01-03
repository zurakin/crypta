def decrypt_letter(letter, code):
    return chr((ord(letter)-ord(code))%128)

def decrypt_sequence(sequence, key):
    newsequence = ''
    for i in range(len(sequence)):
        newsequence += decrypt_letter(sequence[i], key[i%len(key)])
    return newsequence

def verify(content, key):
    for i in range(len(key)):
        if key[i] != content[i]:
            return False
    return True

def decrypt_file(file, key) :
    try:
        with open(file, 'r') as text:
            content = text.read()
        content = decrypt_sequence(content, key)
        if verify(content, key):
            with open(file, 'w') as text:
                text.write(content[len(key):])
                return 'file decryted succesfully'
        else:
            return 'wrong key'
    except:
        return 'error while decrpting'
