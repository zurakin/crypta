import tkinter, crypter, decrypter

window = tkinter.Tk()
window.title('crypta')
window.geometry("250x100")


path_label = tkinter.Label(window, text = 'file path :')
path_label.grid(row = 0, column = 0)
path_text = tkinter.Text(window,height=1,width=20)
path_text.grid(row = 0, column = 1)

key_label = tkinter.Label(window, text = 'crypting key :')
key_label.grid(row = 1, column = 0)
key_text = tkinter.Text(window,height=1,width=20)
key_text.grid(row = 1, column = 1)


def crypt_command():
    result = crypter.crypt_file(path_text.get(1.0, 'end').rstrip(), key_text.get(1.0, 'end').rstrip())
    key_text.delete(1.0, 'end')
    key_text.insert('end', result)

crypt_button = tkinter.Button(window, text = 'crypt', command = crypt_command)
crypt_button.grid(row = 2, column = 0)

def decrypt_command():
    result = decrypter.decrypt_file(path_text.get(1.0, 'end').rstrip(), key_text.get(1.0, 'end').rstrip())
    key_text.delete(1.0, 'end')
    key_text.insert('end', result)

decrypt_button = tkinter.Button(window, text = 'decrypt', command = decrypt_command)
decrypt_button.grid(row = 2, column = 1)

window.mainloop()
