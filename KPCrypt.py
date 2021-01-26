import tkinter as tk
from tkinter import Text, messagebox
import os, sys
import binascii
import base64

root = tk.Tk()
root.title("KPCrypt")
root.resizable(0, 0)
canvas = tk.Canvas(root, height=700, width=700, bg="#25283D")
canvas.pack()

## STARTING SCREEN ##

def startDisplay():
    frame = tk.Frame(root, bg="#25283D")
    frame.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(frame,
                             text="Welcome to KPCrypt",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 38),
                             justify="center")
    welcome_label.place(rely=0.1, relx=0.1)

    descryption = "A cryptography & cryptoanalysis tool\n made for students,\nby students"
    descryption_label = tk.Label(frame,
                                 text=descryption,
                                 fg="#CCDBDC", bg="#25283D",
                                 font=("Courier", 19),
                                 justify="center")
    descryption_label.place(rely=0.2, relx=0.1)

    copyright_label = tk.Label(canvas,
                               text="This program was developed by Kurkotov Alexander and Ann Popova",
                               fg="#CCDBDC", bg="#25283D",
                               font=("Courier", 7),
                               justify="center")
    copyright_label.place(relx=0.01, rely=0.97)

    startButton = tk.Button(frame,
                            text='Start',
                            font=("Courier", 20),
                            padx=10, pady=5,
                            fg="#25283D", bg='#CCDBDC',
                            command=cryptoChoiceDisplay)
    startButton.place(relx=0.39, rely=0.7)
    startButton = tk.Button(frame,
                            text='Exit',
                            font=("Courier", 20),
                            padx=10, pady=5,
                            fg="#25283D", bg='#CCDBDC',
                            command=sys.exit)
    startButton.place(relx=0.4, rely=0.81)

## CHOICE SCREEN ##

def cryptoChoiceDisplay():
    frame = tk.Frame(root, bg="#25283D")
    frame.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(frame,
                             text="Select encryption/encoding",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 28),
                             justify="center")
    welcome_label.place(rely=0.1, relx=0.1)

    hexButton = tk.Button(frame,
                          text='Hex',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=hexDisplay)
    hexButton.place(x=25, y=400)

    baseButton = tk.Button(frame,
                          text='Base64',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=baseDisplay)
    baseButton.place(x=125, y=400)

    rotButton = tk.Button(frame,
                           text='ROT',
                           font=("Courier", 20),
                           padx=10, pady=5,
                           fg="#25283D", bg='#CCDBDC',
                           command=rotDisplay)
    rotButton.place(x=275, y=400)

    rsaButton = tk.Button(frame,
                          text='RSA',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=rsaDisplay)
    rsaButton.place(x=375, y=400)

    s2numButton = tk.Button(frame,
                          text='Str 2 Num',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=s2numDisplay)
    s2numButton.place(x=475, y=400)

    backButton = tk.Button(frame,
                          text='Back',
                          font=("Courier", 15),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=startDisplay)
    backButton.place(x=0, y=0)



def hexDisplay():
    strings = []

    frame = tk.Frame(root, bg="#25283D")
    frame.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(frame,
                             text="Input your hex string to decode\nor a normal string to encode",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 25),
                             justify="center")
    welcome_label.place(rely=0.1, relx=0.07)
    data_entry = tk.Entry(frame,
                          text="test",
                          bg="#CCDBDC", fg="#25283D",
                          font=("Courier", 16),
                          selectbackground="#25283D", selectforeground="#CCDBDC")
    data_entry.place(rely=0.23, relx=0.3)
    def encHex():
        for ansstring in strings:
            ansstring.destroy()

        ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
        ansString.insert(1.0, binascii.hexlify(data_entry.get().encode()).decode())
        strings.append(ansString)
        ansString.place(rely=0.28)
        ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

        scroll = tk.Scrollbar(command=ansString.yview)
        #scroll.pack(side='left', fill='y')
        ansString.config(yscrollcommand=scroll.set)

    encButton = tk.Button(frame,
                          text='Encode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=encHex)

    encButton.place(x=150, y=400)

    def decHex():
        for ansstring in strings:
            ansstring.destroy()
        try:
            ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
            ansString.insert(1.0, binascii.unhexlify(data_entry.get().encode()).decode())
            strings.append(ansString)
            ansString.place(rely=0.28)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

            scroll = tk.Scrollbar(command=ansString.yview)
            ansString.config(yscrollcommand=scroll.set)
        except binascii.Error and UnicodeDecodeError:
            ansString = tk.Text(frame, height=4, borderwidth=0)
            ansString.insert(1.0, "Cannot decode that hex string.\nPlease check input")
            strings.append(ansString)
            ansString.place(rely=0.28)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")
    decButton = tk.Button(frame,
                          text='Decode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=decHex)
    decButton.place(x=400, y=400)
    backButton = tk.Button(frame,
                           text='Back',
                           font=("Courier", 15),
                           padx=10, pady=5,
                           fg="#25283D", bg='#CCDBDC',
                           command=cryptoChoiceDisplay)
    backButton.place(x=0, y=0)

    def detailEncHex():
      for ansstring in strings:
            ansstring.destroy()
      try:
          string = data_entry.get()
          ans = ''''''
          for symbol in string[:5]:
            ans += f"ASCII: {symbol} => DECIMAL: {ord(symbol)} => HEXADECIMAL: {binascii.hexlify(symbol.encode()).decode()}\n"

          if len(string) > 5:
            ans += "...\n"

          ans += "Combining the hex outputs:\n"

          ans += f"End result: {binascii.hexlify(string.encode()).decode()}"
          ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
          ansString.insert(1.0, ans)
          strings.append(ansString)
          ansString.place(rely=0.28)
          ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

          scroll = tk.Scrollbar(command=ansString.yview)
          ansString.config(yscrollcommand=scroll.set)
      except binascii.Error and UnicodeDecodeError:
          ansString = tk.Text(frame, height=4, borderwidth=0)
          ansString.insert(1.0, "Cannot decode that hex string.\nPlease check input")
          strings.append(ansString)
          ansString.place(rely=0.28)
          ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

    detailEncodeButton = tk.Button(frame,
                          text='Encode\n with details',
                          font=("Courier", 11),
                          padx=0, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=detailEncHex)

    detailEncodeButton.place(x=150, y = 450)

    def detailDecHex():
      for ansstring in strings:
            ansstring.destroy()
      try:
          string = data_entry.get()
          ans = ''''''

          for i in range(0, len(string[:10]), 2):
            byte = string[i] + string[i + 1]
            number = int(byte, 16)
            symbol = chr(number)
            ans += f'HEXADECIMAL: {byte} => DECIMAL: {number} => ASCII: {symbol}\n'
          if len(string) > 10:
            ans += "...\n"
          ans += f"End result: {binascii.unhexlify(string).decode()}"

          ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
          ansString.insert(1.0, ans)
          strings.append(ansString)
          ansString.place(rely=0.28)
          ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

          scroll = tk.Scrollbar(command=ansString.yview)
          ansString.config(yscrollcommand=scroll.set)
      except binascii.Error and UnicodeDecodeError:
          ansString = tk.Text(frame, height=4, borderwidth=0)
          ansString.insert(1.0, "Cannot decode that hex string.\nPlease check input")
          strings.append(ansString)
          ansString.place(rely=0.28)
          ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

    detailDecodeButton = tk.Button(frame,
                          text='Decode\n with details',
                          font=("Courier", 11),
                          padx=0, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=detailDecHex)

    detailDecodeButton.place(x=400, y = 450)


def baseDisplay():
    strings = []

    frame = tk.Frame(root, bg="#25283D")
    frame.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(frame,
                             text="Input your base64 string to decode\nor a normal string to encode",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 25),
                             justify="center")
    welcome_label.place(rely=0.1, relx=0.02)
    data_entry = tk.Entry(frame,
                          bg="#CCDBDC", fg="#25283D",
                          font=("Courier", 16),
                          selectbackground="#25283D", selectforeground="#CCDBDC")
    data_entry.place(rely=0.23, relx=0.3)

    def encBase64():
        for ansstring in strings:
            ansstring.destroy()

        ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
        ansString.insert(1.0, base64.b64encode(data_entry.get().encode()).decode())
        strings.append(ansString)
        ansString.place(rely=0.28)
        ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

        scroll = tk.Scrollbar(command=ansString.yview)
        # scroll.pack(side='left', fill='y')
        ansString.config(yscrollcommand=scroll.set)

    encButton = tk.Button(frame,
                          text='Encode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=encBase64)

    encButton.place(x=150, y=400)

    def decBase64():
        for ansstring in strings:
            ansstring.destroy()
        try:
            ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
            ansString.insert(1.0, base64.b64decode(data_entry.get()).decode())
            strings.append(ansString)
            ansString.place(rely=0.28)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

            scroll = tk.Scrollbar(command=ansString.yview)
            ansString.config(yscrollcommand=scroll.set)
        except binascii.Error and UnicodeDecodeError:
            ansString = tk.Text(frame, height=4, borderwidth=0)
            ansString.insert(1.0, "Cannot decode that base string.\nPlease check input")
            strings.append(ansString)
            ansString.place(rely=0.28)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

    decButton = tk.Button(frame,
                          text='Decode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=decBase64)
    decButton.place(x=400, y=400)
    backButton = tk.Button(frame,
                           text='Back',
                           font=("Courier", 15),
                           padx=10, pady=5,
                           fg="#25283D", bg='#CCDBDC',
                           command=cryptoChoiceDisplay)
    backButton.place(x=0, y=0)

def rotDisplay():
    strings = []

    frame = tk.Frame(root, bg="#25283D")
    frame.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(frame,
                             text="Input your string and key\nto encode or decode with",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 25),
                             justify="center")
    welcome_label.place(rely=0.1, relx=0.125)

    string_label = tk.Label(frame,
                             text="String:",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 20),
                             justify="center")
    string_label.place(rely=0.22, relx=0.13)

    key_label = tk.Label(frame,
                            text="Key:",
                            fg="#CCDBDC", bg="#25283D",
                            font=("Courier", 20),
                            justify="center")
    key_label.place(rely=0.29, relx=0.198)

    data_entry = tk.Entry(frame,
                          bg="#CCDBDC", fg="#25283D",
                          font=("Courier", 16),
                          selectbackground="#25283D", selectforeground="#CCDBDC")
    data_entry.place(rely=0.23, relx=0.3)

    key_entry = tk.Entry(frame,
                          bg="#CCDBDC", fg="#25283D",
                          font=("Courier", 16),
                          selectbackground="#25283D", selectforeground="#CCDBDC")
    key_entry.place(rely=0.3, relx=0.3)

    def encRot():
        try:
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            data = data_entry.get()
            key = int(key_entry.get())

            cipher = ''

            for i in range(len(data)):
                if data[i].isupper():
                    letter_index = ALPHA.index(data[i])
                    letter_index += key
                    letter_index %= 26
                    cipher += ALPHA[letter_index]
                elif data[i].islower():
                    letter_index = alpha.index(data[i])
                    letter_index += key
                    letter_index %= 26
                    cipher += alpha[letter_index]
                else:
                    cipher += data[i]

            for ansstring in strings:
                ansstring.destroy()

            ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
            ansString.insert(1.0, cipher)
            strings.append(ansString)
            ansString.place(rely=0.35)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

            scroll = tk.Scrollbar(command=ansString.yview)
            # scroll.pack(side='left', fill='y')
            ansString.config(yscrollcommand=scroll.set)
        except ValueError:
            for ansstring in strings:
                ansstring.destroy()

            ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
            ansString.insert(1.0, "Invalid key, check if it is a number")
            strings.append(ansString)
            ansString.place(rely=0.35)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

    encButton = tk.Button(frame,
                          text='Encode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=encRot)

    encButton.place(x=150, y=400)

    def bruteRot():
        cipher = ''
        for key in range(1, 27):
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            data = data_entry.get()

            cipher += f'\nKey: {key}\n'

            for i in range(len(data)):
                if data[i].isupper():
                    letter_index = ALPHA.index(data[i])
                    letter_index += key
                    letter_index %= 26
                    cipher += ALPHA[letter_index]
                elif data[i].islower():
                    letter_index = alpha.index(data[i])
                    letter_index += key
                    letter_index %= 26
                    cipher += alpha[letter_index]
                else:
                    cipher += data[i]



        for ansstring in strings:
            ansstring.destroy()

        ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
        ansString.insert(1.0, cipher)
        strings.append(ansString)
        ansString.place(rely=0.35)
        ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

        scroll = tk.Scrollbar(command=ansString.yview)
        # scroll.pack(side='left', fill='y')
        ansString.config(yscrollcommand=scroll.set)

    decButton = tk.Button(frame,
                          text='Bruteforce',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=bruteRot)
    decButton.place(x=400, y=400)

    backButton = tk.Button(frame,
                           text='Back',
                           font=("Courier", 15),
                           padx=10, pady=5,
                           fg="#25283D", bg='#CCDBDC',
                           command=cryptoChoiceDisplay)
    backButton.place(x=0, y=0)

def rsaDisplay():
    strings = []

    frame = tk.Frame(root, bg="#25283D")
    frame.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(frame,
                             text="Input your data and keys\nto encode or decode with",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 25),
                             justify="center")
    welcome_label.place(rely=0.1, relx=0.1)

    string_label = tk.Label(frame,
                            text="Data:",
                            fg="#CCDBDC", bg="#25283D",
                            font=("Courier", 20),
                            justify="center")
    string_label.place(rely=0.22, relx=0.125)

    e_label = tk.Label(frame,
                         text="e:",
                         fg="#CCDBDC", bg="#25283D",
                         font=("Courier", 20),
                         justify="center")
    e_label.place(rely=0.29, relx=0.225)

    d_label = tk.Label(frame,
                       text="d:",
                       fg="#CCDBDC", bg="#25283D",
                       font=("Courier", 20),
                       justify="center")
    d_label.place(rely=0.29, relx=0.425)

    n_label = tk.Label(frame,
                       text="n:",
                       fg="#CCDBDC", bg="#25283D",
                       font=("Courier", 20),
                       justify="center")
    n_label.place(rely=0.29, relx=0.625)

    data_entry = tk.Entry(frame,
                          width=27,
                          bg="#CCDBDC", fg="#25283D",
                          font=("Courier", 16),
                          selectbackground="#25283D", selectforeground="#CCDBDC")
    data_entry.place(rely=0.23, relx=0.275)

    e_entry = tk.Entry(frame,
                         width=5,
                         bg="#CCDBDC", fg="#25283D",
                         font=("Courier", 16),
                         selectbackground="#25283D", selectforeground="#CCDBDC")
    e_entry.place(rely=0.3, relx=0.275)

    d_entry = tk.Entry(frame,
                       width=5,
                       bg="#CCDBDC", fg="#25283D",
                       font=("Courier", 16),
                       selectbackground="#25283D", selectforeground="#CCDBDC")
    d_entry.place(rely=0.3, relx=0.475)

    n_entry = tk.Entry(frame,
                       width=5,
                       bg="#CCDBDC", fg="#25283D",
                       font=("Courier", 16),
                       selectbackground="#25283D", selectforeground="#CCDBDC")
    n_entry.place(rely=0.3, relx=0.675)

    def encRSA():
        data = int(data_entry.get())
        e = int(e_entry.get())
        n = int(n_entry.get())

        cipher = (data ** e) % n

        ansString = tk.Text(frame, height=3, borderwidth=0, width=58)
        ansString.insert(1.0, cipher)
        strings.append(ansString)
        ansString.place(rely=0.35)
        ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

        scroll = tk.Scrollbar(command=ansString.yview)
        # scroll.pack(side='left', fill='y')
        ansString.config(yscrollcommand=scroll.set)


    encButton = tk.Button(frame,
                          text='Encode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=encRSA)
    encButton.place(x=150, y=400)

    def decRSA():
        data = int(data_entry.get())
        d = int(d_entry.get())
        n = int(n_entry.get())

        cipher = (data ** d) % n

        ansString = tk.Text(frame, height=3, borderwidth=0, width=58)
        ansString.insert(1.0, cipher)
        strings.append(ansString)
        ansString.place(rely=0.35)
        ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

        scroll = tk.Scrollbar(command=ansString.yview)
        # scroll.pack(side='left', fill='y')
        ansString.config(yscrollcommand=scroll.set)

    decButton = tk.Button(frame,
                          text='Decode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=decRSA)
    decButton.place(x=400, y=400)

    backButton = tk.Button(frame,
                           text='Back',
                           font=("Courier", 15),
                           padx=10, pady=5,
                           fg="#25283D", bg='#CCDBDC',
                           command=cryptoChoiceDisplay)
    backButton.place(x=0, y=0)

def s2numDisplay():
    strings = []

    frame = tk.Frame(root, bg="#25283D")
    frame.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(frame,
                             text="Input your string to encode into a number\nor a number to decode",
                             fg="#CCDBDC", bg="#25283D",
                             font=("Courier", 25),
                             justify="center")
    welcome_label.place(rely=0.1, relx=0.07)
    data_entry = tk.Entry(frame,
                          text="test",
                          bg="#CCDBDC", fg="#25283D",
                          font=("Courier", 16),
                          selectbackground="#25283D", selectforeground="#CCDBDC")
    data_entry.place(rely=0.23, relx=0.3)

    def encHex():
        for ansstring in strings:
            ansstring.destroy()

        ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
        ansString.insert(1.0, int(binascii.hexlify(data_entry.get().encode()).decode(), 16))
        strings.append(ansString)
        ansString.place(rely=0.28)
        ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

        scroll = tk.Scrollbar(command=ansString.yview)
        # scroll.pack(side='left', fill='y')
        ansString.config(yscrollcommand=scroll.set)

    encButton = tk.Button(frame,
                          text='Encode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=encHex)

    encButton.place(x=150, y=400)

    def decHex():
        for ansstring in strings:
            ansstring.destroy()
        try:
            ansString = tk.Text(frame, height=5, borderwidth=0, width=58)
            ansString.insert(1.0, binascii.unhexlify(hex(int(data_entry.get()))[2:].encode()).decode())
            strings.append(ansString)
            ansString.place(rely=0.28)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

            scroll = tk.Scrollbar(command=ansString.yview)
            ansString.config(yscrollcommand=scroll.set)
        except binascii.Error and UnicodeDecodeError:
            ansString = tk.Text(frame, height=4, borderwidth=0)
            ansString.insert(1.0, "Cannot decode that hex string.\nPlease check input")
            strings.append(ansString)
            ansString.place(rely=0.28)
            ansString.configure(state="disabled", font=("Courier", 15), fg="#CCDBDC", bg="#25283D")

    decButton = tk.Button(frame,
                          text='Decode',
                          font=("Courier", 20),
                          padx=10, pady=5,
                          fg="#25283D", bg='#CCDBDC',
                          command=decHex)
    decButton.place(x=400, y=400)

    backButton = tk.Button(frame,
                           text='Back',
                           font=("Courier", 15),
                           padx=10, pady=5,
                           fg="#25283D", bg='#CCDBDC',
                           command=cryptoChoiceDisplay)
    backButton.place(x=0, y=0)

startDisplay()

root.mainloop()