import tkinter as tk
from tkinter import ttk
from tkinter import *


def show_info():
    window = Toplevel(root)
    window.title("СПРАВКА")
    window.minsize(width=353, height=280)
    window.maxsize(width=353, height=280)
    window = Label(window, fg="pale goldenrod", bg="black", font="Verdana 15", justify=LEFT,
                   text='       Программа-шифровальщик\nДанная программа реализует\n\
алгоритмы шифрования:\n - cдвиг Цезаря\n - шифр Атбаш \n - шифр Виженера\n - квадрат Плейфера\n - метод Полибия \nПрограмму написал \nОлег Владимирович Ярославский \nв 2025 году.')
    window.pack()


def caesar_cipher():

    def show_caesar_help():
        window = Toplevel(caesar_root)
        window.title("СПРАВКА")
        window.minsize(width=601, height=300)
        window.maxsize(width=601, height=300)
        window = Label(window, fg="pale goldenrod", bg="black", font="Verdana 15", justify=LEFT,
                       text=r"                      СПРАВКА - СДВИГ ЦЕЗАРЯ" "\n"
                            "Сдвиг Цезаря – один из самых древних шифров \nV – IV веков до н. э. Шиф"
                            "р назван в честь римского\nимператора Гая Юлия Цезаря. При шифровании\nкаждый символ заменяется другим, стоящим\nот него в алфавите на k число позиций.\n\nАлгоритм шифрует русские и английские буквы, цифры.\nОстальные символы (.,!?*\\& и д"
                            "р.) не шифруются.\nШифр Цезаря имеет простую реализацию; но его легко\nвзломать, просто перебрав все возможные значения\nсдвигов (ведь их не больше, чем букв в алфавите).")
        window.pack()

    def darken_help_button(event):
        event.widget.config(bg='grey20')

    def lighten_help_button(event):
        event.widget.config(bg='grey11')

    def encrypt():
        message = message_input.get(1.0, END)
        shift = int(shift_input.get(1.0, END))
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ012345678901234567890123456789012345678901234567890123456789'
        result = str("")
        while message[len(message) - 1] == " ":
            message = message[:-1]
        for char in message:
            position = alphabet.find(char)
            new_position = position + shift
            if char in alphabet:
                result += alphabet[new_position]
            else:
                result += char
        output.insert(1.0, result + "\n")

    def decrypt():
        message = message_input.get(1.0, END)
        shift = int(shift_input.get(1.0, END))
        alphabet = '012345678901234567890123456789012345678901234567890123456789ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        result = str("")
        while message[len(message) - 1] == " ":
            message = message[:-1]
        for char in message:
            position = alphabet.rfind(char)
            new_position = position - shift
            if char in alphabet:
                result += alphabet[new_position]
            else:
                result += char
        output.insert(1.0, result + "\n")

    caesar_root = Tk()
    caesar_root.title("ШИФРОВАЛЬЩИК - СДВИГ ЦЕЗАРЯ")
    caesar_root.geometry("800x800")
    caesar_root.minsize(width=800, height=800)
    caesar_root.maxsize(width=800, height=800)

    top_frame = Frame(caesar_root, width=190, height=130, bd=5, bg="cyan2")
    top_frame.pack()

    shift_label = Label(top_frame, fg="pale goldenrod", text="Введите шаг", bg="black", width=100, font="Verdana 15")
    shift_label.pack()

    shift_input = Text(top_frame, width=100, fg="yellow", font="Verdana 15", bg="black", height=1)
    shift_input.pack()

    message_label = Label(top_frame, fg="pale goldenrod", text="Введите сообщение", bg="black", width=70, font="Verdana 15")
    message_label.pack()

    message_input = Text(top_frame, height=9, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    message_input.pack()

    buttons_frame = Frame(caesar_root, width=190, height=100, bd=5, bg="cyan2")
    buttons_frame.pack()

    encrypt_button = Button(buttons_frame, command=encrypt, text="Зашифровать", fg="yellow", font="Verdana 15", width=30, height=2, bg="grey11")
    encrypt_button.grid(row=0, column=0)

    decrypt_button = Button(buttons_frame, command=decrypt, text="Расшифровать", fg="yellow", font="Verdana 15", width=29, height=2, bg="grey11")
    decrypt_button.grid(row=0, column=1)

    output_frame = Frame(caesar_root, width=190, height=130, bd=5, bg="cyan2")
    output_frame.pack()

    output = Text(output_frame, height=12, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    output.pack()

    help_button = Button(top_frame, command=show_caesar_help, text="i", fg="yellow", font="Verdana 15", bg="grey11", width=2, height=1)
    help_button.place(x=749, y=5)
    help_button.bind('<Enter>', darken_help_button)
    help_button.bind('<Leave>', lighten_help_button)

    caesar_root.mainloop()


def atbash_cipher():

    def show_atbash_help():
        window = Toplevel(atbash_root)
        window.title("СПРАВКА")
        window.minsize(width=621, height=280)
        window.maxsize(width=621, height=280)
        window = Label(window, fg="pale goldenrod", bg="black", font="Verdana 15", justify=LEFT,
                       text=r'                      СПРАВКА - ШИФР АТБАШ ' "\n"
                            "Шифр Атбаша – это шифр простой замены, впе"
                            "рвые\nиспользованный для еврейского алфавита VI - XIV н.э. \nШифрование происходит заменой первой буквы алфавита\nна последнюю, второй на предпоследнюю и т.д.\n\nАлгоритм шифрует русские и английские буквы, цифр"
                            "ы.\nОстальные символы (.,!?*\\& и др.) не шифруются.\nЭтот шифр является одним из самых простых, его очень \nлегко разгадать; очень прост в реализации.\nОбъем зашифрованных данных не изменяется.")
        window.pack()

    def darken_help_button(event):
        event.widget.config(bg='grey20')

    def lighten_help_button(event):
        event.widget.config(bg='grey11')

    def encrypt():
        message = message_input.get(1.0, END)
        alphabet = r'.,?!+-="%;№@ :\|/$#абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        reversed_alphabet = '$#-+= |\\"/%?!№@:;,.яюэьыъщшчцхфутсрпонмлкйизжёедгвбаЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБАzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA9876543210'
        result = str("")
        while message[len(message) - 1] == " ":
            message = message[:-1]
        for char in message:
            position = alphabet.find(char)
            if char in alphabet:
                result += reversed_alphabet[position]
            else:
                result += char
        output.insert(1.0, result + "\n")

    def decrypt():
        message = message_input.get(1.0, END)
        alphabet = r'.,?!+-="%;№@ :\|/$#абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        reversed_alphabet = '$#-+= |\\"/%?!№@:;,.яюэьыъщшчцхфутсрпонмлкйизжёедгвбаЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБАzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA9876543210'
        result = str("")
        while message[len(message) - 1] == " ":
            message = message[:-1]

        for char in message:
            position = reversed_alphabet.find(char)
            if char in alphabet:
                result += alphabet[position]
            else:
                result += char
        output.insert(1.0, result + "\n")

    atbash_root = Tk()
    atbash_root.title("ШИФРОВАЛЬЩИК - ШИФР АТБАШ")
    atbash_root.geometry("800x800")
    atbash_root.minsize(width=800, height=800)
    atbash_root.maxsize(width=800, height=800)

    top_frame = Frame(atbash_root, width=190, height=130, bd=5, bg="cyan2")
    top_frame.pack()

    message_label = Label(top_frame, fg="pale goldenrod", text="Введите сообщение", bg="black", width=70, font="Verdana 15")
    message_label.pack()

    message_input = Text(top_frame, height=9, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    message_input.pack()

    buttons_frame = Frame(atbash_root, width=190, height=100, bd=5, bg="cyan2")
    buttons_frame.pack()

    encrypt_button = Button(buttons_frame, command=encrypt, text="Зашифровать", fg="yellow", font="Verdana 15", width=30, height=2, bg="grey11")
    encrypt_button.grid(row=0, column=0)

    decrypt_button = Button(buttons_frame, command=decrypt, text="Расшифровать", fg="yellow", font="Verdana 15", width=29, height=2, bg="grey11")
    decrypt_button.grid(row=0, column=1)

    output_frame = Frame(atbash_root, width=190, height=130, bd=5, bg="cyan2")
    output_frame.pack()

    output = Text(output_frame, height=12, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    output.pack()

    help_button = Button(top_frame, command=show_atbash_help, text="i", fg="yellow", font="Verdana 15", bg="grey11", width=2, height=1)
    help_button.place(x=749, y=5)
    help_button.bind('<Enter>', darken_help_button)
    help_button.bind('<Leave>', lighten_help_button)

    atbash_root.mainloop()


def vigenere_cipher():
    def show_vigenere_help():
        window = Toplevel(vigenere_root)
        window.title("СПРАВКА")
        window.minsize(width=591, height=330)
        window.maxsize(width=591, height=330)
        window = Label(window, fg="pale goldenrod", bg="black", font="Verdana 15", justify=LEFT,
                       text='                СПРАВКА - ШИФР ВИЖЕНЕРА\nШифр Виженера – это метод шифрования  текста \nс использованием кодового слова. \nНазванный именем францу'
                            'зского дипломата XVI века, \nон был изобретен независимо друг от друга разными\nлюдьми. Что интересно, Блеза Виженера при этом\nсреди них не было, он лишь убедил Генриха III\nиспользовать его. Название шифр получил в XIX веке.\n\nДля работы алгоритма нужно кодовое слово. \nПри ши'
                            'фровании n-ная буква сообщения заменяется \nна символ, стоящий на k позиций правее, \nгде k – место в алфавите n-ной буквы в кодовом слове.')
        window.pack()

    def darken_help_button(event):
        event.widget.config(bg='grey20')

    def lighten_help_button(event):
        event.widget.config(bg='grey11')

    def encrypt():
        message = message_input.get(1.0, END)
        message = message.lower()
        message = message.replace("\n", " ")
        keyword = keyword_input.get(1.0, END)
        keyword = keyword.lower()
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmn.,?!:;()%$#@ "\\-0123456789.,?!:;()%$#@ "\\-0123456789.,?!:;()%$#@ "\\-0123456789'
        russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = str("")
        keyword_position = 0

        while message[len(message) - 1] == " ":
            message = message[:-1]

        for char in message:

            while keyword_position > int(len(message)):
                keyword_position -= 1
            if int(len(keyword)) < int(len(message)) and keyword_position == int(len(keyword)) - 1:
                keyword_position = 0

            if char in alphabet:
                keyword_char = str(keyword[keyword_position])

                if keyword_char in russian_alphabet:
                    shift = russian_alphabet.find(keyword_char)
                    position = alphabet.find(char)
                    new_position = position + shift
                    result += alphabet[new_position]
                    keyword_position += 1
                elif keyword_char in english_alphabet:
                    shift = english_alphabet.find(keyword_char)
                    position = alphabet.find(char)
                    new_position = position + shift
                    result += alphabet[new_position]
                    keyword_position += 1
            else:
                result += char

        output.insert(1.0, result + "\n\n")

    def decrypt():
        message = message_input.get(1.0, END)
        keyword = keyword_input.get(1.0, END)
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmn.,?!:;()%$#@ "\\-0123456789.,?!:;()%$#@ "\\-0123456789.,?!:;()%$#@ "\\-0123456789'
        russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = str("")
        keyword_position = 0
        while message[len(message) - 1] == " ":
            message = message[:-1]

        for char in message:

            while keyword_position > int(len(message)):
                keyword_position -= 1
            if int(len(keyword)) < int(len(message)) and keyword_position == int(len(keyword)) - 1:
                keyword_position = 0

            if char in alphabet:
                keyword_char = str(keyword[keyword_position])

                if keyword_char in russian_alphabet:
                    shift = russian_alphabet.find(keyword_char)
                    position = alphabet.rfind(char)
                    new_position = position - shift
                    result += alphabet[new_position]
                    keyword_position += 1
                elif keyword_char in english_alphabet:
                    shift = english_alphabet.find(keyword_char)
                    position = alphabet.rfind(char)
                    new_position = position - shift
                    result += alphabet[new_position]
                    keyword_position += 1
            else:
                result += char

        output.insert(1.0, result + "\n\n")

    vigenere_root = Tk()
    vigenere_root.title("ШИФРОВАЛЬЩИК - ШИФР ВИЖЕНЕРА")
    vigenere_root.geometry("800x800")
    vigenere_root.minsize(width=800, height=800)
    vigenere_root.maxsize(width=800, height=800)

    top_frame = Frame(vigenere_root, width=190, height=130, bd=5, bg="cyan2")
    top_frame.pack()

    keyword_label = Label(top_frame, fg="pale goldenrod", text="Введите кодовое слово", bg="black", width=100, font="Verdana 15")
    keyword_label.pack()

    keyword_input = Text(top_frame, width=100, fg="yellow", font="Verdana 15", bg="black", height=1, wrap="word")
    keyword_input.pack()

    message_label = Label(top_frame, fg="pale goldenrod", text="Введите сообщение", bg="black", width=70, font="Verdana 15")
    message_label.pack()

    message_input = Text(top_frame, height=9, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    message_input.pack()

    buttons_frame = Frame(vigenere_root, width=190, height=100, bd=5, bg="cyan2")
    buttons_frame.pack()

    encrypt_button = Button(buttons_frame, command=encrypt, text="Зашифровать", fg="yellow", font="Verdana 15", width=30, height=2, bg="grey11")
    encrypt_button.grid(row=0, column=0)

    decrypt_button = Button(buttons_frame, command=decrypt, text="Расшифровать", fg="yellow", font="Verdana 15", width=29, height=2, bg="grey11")
    decrypt_button.grid(row=0, column=1)

    output_frame = Frame(vigenere_root, width=190, height=130, bd=5, bg="cyan2")
    output_frame.pack()

    output = Text(output_frame, height=12, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    output.pack()

    help_button = Button(top_frame, command=show_vigenere_help, text="i", fg="yellow", font="Verdana 15", bg="grey11", width=2, height=1)
    help_button.place(x=749, y=5)
    help_button.bind('<Enter>', darken_help_button)
    help_button.bind('<Leave>', lighten_help_button)

    vigenere_root.mainloop()


def playfair_cipher():
    def show_playfair_help():
        window = Toplevel(playfair_root)
        window.title("СПРАВКА")
        window.minsize(width=565, height=355)
        window.maxsize(width=565, height=355)
        window = Label(window, fg="pale goldenrod", bg="black", font="Verdana 15", justify=LEFT,
                       text='           СПРАВКА - КВАДРАТ ПЛЕЙФЕРА\nВ начале 1850-х гг. Чарльз Уитстон придумал\nтак называемый «прямоугольный шифр».\nЛеон Плейфер, его близкий друг, рассказал об этом\nшифре во время встречи министру внутренних дел \nлорду Пальмерстону.\n\nДля шифрования создается кодовое слово \nи таблица - русская 4x8, английская 5x5. \nТаблица заполняется сначала кодом, а затем\nостальными буквами. Повторяющиеся буквы\nв таблице удаляются. Далее сообщение разбивается \nпо две буквы, которые шифруются в зависимости от\nих положения в таблице.')
        window.pack()

    def darken_help_button(event):
        event.widget.config(bg='grey20')

    def lighten_help_button(event):
        event.widget.config(bg='grey11')

    def encrypt():
        message = message_input.get(1.0, END)
        message = message.lower()
        message_buffer = ""
        keyword = keyword_input.get(1.0, END)
        keyword = keyword.lower()
        result = str("")
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя0123456789.,!?:; &%#"-+$'
        combined = (str(keyword[:-1]) + str(alphabet))
        alphabet = ''
        special_chars, special_positions = [], []
        count = 0

        for i in range(len(combined)):
            if alphabet.find(combined[i]) == -1:
                alphabet += combined[i]

        message = message.lower()

        message = message.replace("\n", " ")
        while message[len(message) - 1] == " ":
            message = message[:-1]

        for i in range(0, len(message)):
            if message[i] in alphabet:
                message_buffer += message[i]
            else:
                special_chars += [message[i]]
                special_positions += [count]
            count += 1

        message = message_buffer
        message_buffer = ""

        if (len(message)) % 2 == 1:
            message += "я"
        print(message)

        for i in range(0, len(message), 2):
            if message[i] == message[i + 1]:
                message_buffer = message_buffer + message[i] + "яя" + message[i + 1]
            else:
                message_buffer = message_buffer + message[i] + message[i + 1]

        message = message_buffer

        for i in range(0, len(message), 2):
            position1 = alphabet.find(message[i])
            position2 = alphabet.find(message[i + 1])
            if position1 % 8 == position2 % 8:
                if position1 + 8 >= 56:
                    position1 = position1 - 56
                if position2 + 8 >= 56:
                    position2 = position2 - 56
                result = result + alphabet[position1 + 8] + alphabet[position2 + 8]
            elif (0 <= position1 < 8 and 0 <= position2 < 8) or (8 <= position1 < 16 and 8 <= position2 < 16) \
                    or (16 <= position1 < 24 and 16 <= position2 < 24) or (24 <= position1 < 32 and 24 <= position2 < 32) \
                    or (32 <= position1 < 40 and 32 <= position2 < 40) or (40 <= position1 < 48 and 40 <= position2 < 48) \
                    or (48 <= position1 < 56 and 48 <= position2 < 56):
                if position1 + 1 == 8 or position1 + 1 == 16 or position1 + 1 == 24 or position1 + 1 == 32 or position1 + 1 == 39 \
                        or position1 + 1 == 48 or position1 + 1 == 56:
                    position1 = position1 - 8
                if position2 + 1 == 8 or position2 + 1 == 16 or position2 + 1 == 24 or position2 + 1 == 32 or position2 + 1 == 39 \
                        or position2 + 1 == 48 or position2 + 1 == 56:
                    position2 = position2 - 8
                result = result + alphabet[position1 + 1] + alphabet[position2 + 1]
            else:
                if ((0 <= position1 < 8 and 8 <= position2 < 16) or (8 <= position1 < 16 and 16 <= position2 < 24)
                        or (16 <= position1 < 24 and 24 <= position2 < 32) or (32 <= position1 < 40 and 40 <= position2 < 48)
                        or (40 <= position1 < 48 and 48 <= position2 < 56) or (0 <= position2 < 8 and 8 <= position1 < 16)
                        or (8 <= position2 < 16 and 16 <= position1 < 24) or (16 <= position2 < 24 and 24 <= position1 < 32)
                        or (32 <= position2 < 40 and 40 <= position1 < 48) or (40 <= position2 < 48 and 48 <= position1 < 56)):
                    if position2 > position1:
                        result = result + alphabet[position2 - 8] + alphabet[position1 + 8]
                    else:
                        result = result + alphabet[position2 + 8] + alphabet[position1 - 8]

                if (0 <= position1 < 8 and 16 <= position2 < 24) or (8 <= position1 < 16 and 24 <= position2 < 32) \
                        or (24 <= position1 < 32 and 40 <= position2 < 48) or (32 <= position1 < 40 and 48 <= position2 < 56) \
                        or (0 <= position2 < 8 and 16 <= position1 < 24) or (8 <= position2 < 16 and 24 <= position1 < 32) \
                        or (24 <= position2 < 32 and 40 <= position1 < 48) or (32 <= position2 < 40 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 16] + alphabet[position1 + 16]
                    else:
                        result = result + alphabet[position2 + 16] + alphabet[position1 - 16]

                if (0 <= position1 < 8 and 24 <= position2 < 32) or (8 <= position1 < 16 and 32 <= position2 < 40) \
                        or (16 <= position1 < 24 and 40 <= position2 < 48) or (24 <= position1 < 32 and 48 <= position2 < 56) \
                        or (0 <= position2 < 8 and 24 <= position1 < 32) or (8 <= position2 < 16 and 32 <= position1 < 40) \
                        or (16 <= position2 < 24 and 40 <= position1 < 48) or (24 <= position2 < 32 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 24] + alphabet[position1 + 24]
                    else:
                        result = result + alphabet[position2 + 24] + alphabet[position1 - 24]

                if (0 <= position1 < 8 and 32 <= position2 < 40) or (8 <= position1 < 16 and 40 <= position2 < 48) \
                        or (16 <= position1 < 24 and 48 <= position2 < 56) or (0 <= position2 < 8 and 32 <= position1 < 40) \
                        or (8 <= position2 < 16 and 40 <= position1 < 48) or (16 <= position2 < 24 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 32] + alphabet[position1 + 32]
                    else:
                        result = result + alphabet[position2 + 32] + alphabet[position1 - 32]

                if (0 <= position1 < 8 and 40 <= position2 < 48) or (8 <= position1 < 16 and 48 <= position2 < 56) \
                        or (0 <= position2 < 8 and 40 <= position2 < 48) or (8 <= position2 < 16 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 40] + alphabet[position1 + 40]
                    else:
                        result = result + alphabet[position2 + 40] + alphabet[position1 - 40]

                if (0 <= position1 < 8 and 47 <= position2 < 56) or (0 <= position2 < 8 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 48] + alphabet[position1 + 48]
                    else:
                        result = result + alphabet[position2 + 48] + alphabet[position1 - 48]

        result_buffer = ''
        count = 0
        if special_positions != []:
            for i in range(0, len(result)):

                if i == special_positions[count]:

                    result_buffer = result_buffer + special_chars[count] + result[i]

                    if count < len(special_positions) - 1:
                        count += 1

                else:
                    result_buffer += result[i]

            result = result_buffer

        output.insert(1.0, result + "\n\n")

    def decrypt():
        message = message_input.get(1.0, END)
        message = message.lower()
        message_buffer = ""
        keyword = keyword_input.get(1.0, END)
        keyword = keyword.lower()
        result = str("")
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя0123456789.,!?:; &%#"-+$'
        combined = (str(keyword[:-1]) + str(alphabet))
        alphabet = ''
        special_chars, special_positions = [], []
        count = 0

        for i in range(len(combined)):
            if alphabet.find(combined[i]) == -1:
                alphabet += combined[i]

        message = message.replace("\n", " ")
        while message[len(message) - 1] == " ":
            message = message[:-1]

        for i in range(0, len(message)):
            if message[i] in alphabet:
                message_buffer += message[i]
            else:
                special_chars += [message[i]]
                special_positions += [count]
            count += 1

        message = message_buffer
        message_buffer = ""

        for i in range(0, len(message), 2):
            position1 = alphabet.find(message[i])
            position2 = alphabet.find(message[i + 1])
            if position1 % 8 == position2 % 8:
                if position1 - 8 < 0:
                    position1 = position1 + 56
                if position2 - 8 < 0:
                    position2 = position2 + 56
                result = result + alphabet[position1 - 8] + alphabet[position2 - 8]

            elif (0 <= position1 < 8 and 0 <= position2 < 8) or (8 <= position1 < 16 and 8 <= position2 < 16) \
                    or (16 <= position1 < 24 and 16 <= position2 < 24) or (24 <= position1 < 32 and 24 <= position2 < 32) \
                    or (32 <= position1 < 40 and 32 <= position2 < 40) or (40 <= position1 < 48 and 40 <= position2 < 48) \
                    or (48 <= position1 < 56 and 48 <= position2 < 56):
                if position1 - 1 == -1 or position1 - 1 == 7 or position1 - 1 == 15 or position1 - 1 == 23 or position1 - 1 == 31 \
                        or position1 - 1 == 39 or position1 - 1 == 47:
                    position1 = position1 + 8
                if position2 - 1 == -1 or position2 - 1 == 7 or position2 - 1 == 15 or position2 - 1 == 23 or position2 - 1 == 31 \
                        or position2 - 1 == 39 or position2 - 1 == 47:
                    position2 = position2 + 8
                result = result + alphabet[position1 - 1] + alphabet[position2 - 1]

            else:

                if ((0 <= position1 < 8 and 8 <= position2 < 16) or (8 <= position1 < 16 and 16 <= position2 < 24)
                        or (16 <= position1 < 24 and 24 <= position2 < 32) or (32 <= position1 < 40 and 40 <= position2 < 48)
                        or (40 <= position1 < 48 and 48 <= position2 < 56) or (0 <= position2 < 8 and 8 <= position1 < 16)
                        or (8 <= position2 < 16 and 16 <= position1 < 24) or (16 <= position2 < 24 and 24 <= position1 < 32)
                        or (32 <= position2 < 40 and 40 <= position1 < 48) or (40 <= position2 < 48 and 48 <= position1 < 56)):
                    if position2 > position1:
                        result = result + alphabet[position2 - 8] + alphabet[position1 + 8]
                    else:
                        result = result + alphabet[position2 + 8] + alphabet[position1 - 8]

                if (0 <= position1 < 8 and 16 <= position2 < 24) or (8 <= position1 < 16 and 24 <= position2 < 32) \
                        or (24 <= position1 < 32 and 40 <= position2 < 48) or (32 <= position1 < 40 and 48 <= position2 < 56) \
                        or (0 <= position2 < 8 and 16 <= position1 < 24) or (8 <= position2 < 16 and 24 <= position1 < 32) \
                        or (24 <= position2 < 32 and 40 <= position1 < 48) or (32 <= position2 < 40 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 16] + alphabet[position1 + 16]
                    else:
                        result = result + alphabet[position2 + 16] + alphabet[position1 - 16]

                if (0 <= position1 < 8 and 24 <= position2 < 32) or (8 <= position1 < 16 and 32 <= position2 < 40) \
                        or (16 <= position1 < 24 and 40 <= position2 < 48) or (24 <= position1 < 32 and 48 <= position2 < 56) \
                        or (0 <= position2 < 8 and 24 <= position1 < 32) or (8 <= position2 < 16 and 32 <= position1 < 40) \
                        or (16 <= position2 < 24 and 40 <= position1 < 48) or (24 <= position2 < 32 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 24] + alphabet[position1 + 24]
                    else:
                        result = result + alphabet[position2 + 24] + alphabet[position1 - 24]

                if (0 <= position1 < 8 and 32 <= position2 < 40) or (8 <= position1 < 16 and 40 <= position2 < 48) \
                        or (16 <= position1 < 24 and 48 <= position2 < 56) or (0 <= position2 < 8 and 32 <= position1 < 40) \
                        or (8 <= position2 < 16 and 40 <= position1 < 48) or (16 <= position2 < 24 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 32] + alphabet[position1 + 32]
                    else:
                        result = result + alphabet[position2 + 32] + alphabet[position1 - 32]

                if (0 <= position1 < 8 and 40 <= position2 < 48) or (8 <= position1 < 16 and 48 <= position2 < 56) \
                        or (0 <= position2 < 8 and 40 <= position2 < 48) or (8 <= position2 < 16 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 40] + alphabet[position1 + 40]
                    else:
                        result = result + alphabet[position2 + 40] + alphabet[position1 - 40]

                if (0 <= position1 < 8 and 48 <= position2 < 56) or (0 <= position2 < 8 and 48 <= position1 < 56):
                    if position2 > position1:
                        result = result + alphabet[position2 - 48] + alphabet[position1 + 48]
                    else:
                        result = result + alphabet[position2 + 48] + alphabet[position1 - 48]

        result_buffer = ''
        count = 0
        if special_positions != []:
            for i in range(0, len(result)):

                if i == special_positions[count]:

                    result_buffer = result_buffer + special_chars[count] + result[i]

                    if count < len(special_positions) - 1:
                        count += 1

                else:
                    result_buffer += result[i]

            result = result_buffer

        result = result.replace("яя", "")
        output.insert(1.0, result + "\n\n")

    playfair_root = Tk()
    playfair_root.title("ШИФРОВАЛЬЩИК - КВАДРАТ ПЛЕЙФЕРА")
    playfair_root.geometry("800x800")
    playfair_root.minsize(width=800, height=800)
    playfair_root.maxsize(width=800, height=800)

    top_frame = Frame(playfair_root, width=190, height=130, bd=5, bg="cyan2")
    top_frame.pack()

    keyword_label = Label(top_frame, fg="pale goldenrod", text="Введите кодовое слово", bg="black", width=100, font="Verdana 15")
    keyword_label.pack()

    keyword_input = Text(top_frame, width=100, fg="yellow", font="Verdana 15", bg="black", height=1)
    keyword_input.pack()

    message_label = Label(top_frame, fg="pale goldenrod", text="Введите сообщение", bg="black", width=70, font="Verdana 15")
    message_label.pack()

    message_input = Text(top_frame, height=9, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    message_input.pack()

    buttons_frame = Frame(playfair_root, width=190, height=100, bd=5, bg="cyan2")
    buttons_frame.pack()

    encrypt_button = Button(buttons_frame, command=encrypt, text="Зашифровать", fg="yellow", font="Verdana 15", width=30, height=2, bg="grey11")
    encrypt_button.grid(row=0, column=0)

    decrypt_button = Button(buttons_frame, command=decrypt, text="Расшифровать", fg="yellow", font="Verdana 15", width=29, height=2, bg="grey11")
    decrypt_button.grid(row=0, column=1)

    output_frame = Frame(playfair_root, width=190, height=130, bd=5, bg="cyan2")
    output_frame.pack()

    output = Text(output_frame, height=12, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    output.pack()

    help_button = Button(top_frame, command=show_playfair_help, text="i", fg="yellow", font="Verdana 15", bg="grey11", width=2, height=1)
    help_button.place(x=749, y=5)
    help_button.bind('<Enter>', darken_help_button)
    help_button.bind('<Leave>', lighten_help_button)

    playfair_root.mainloop()


def polybius_cipher():
    def show_polybius_help():
        window = Toplevel(polybius_root)
        window.title("СПРАВКА")
        window.minsize(width=556, height=330)
        window.maxsize(width=556, height=330)
        window = Label(window, fg="pale goldenrod", bg="black", font="Verdana 15", justify=LEFT,
                       text='                   СПРАВКА - МЕТОД ПОЛИБИЯ\nМетод Полибия – шифр замены III век до н. э.\nДля ши'
                            'фрования создается таблица 4x8. Она\nзаполняется буквами алфавита (без Ё), и каждому\nсимволу присваиваются номер столбца и номер\nстроки. Сообщение преобразуется в координаты,\nкоторые записываются вертикально, а считыва'
                            'ются\nгоризонтально. Далее координаты преобразуются\nв буквы по изначальной таблице. \n\nШифр Полибия имеет хорошую криптостойкость и\nпростую реализацию, но требует создания\nнескольких таблиц.')
        window.pack()

    def darken_help_button(event):
        event.widget.config(bg='grey20')

    def lighten_help_button(event):
        event.widget.config(bg='grey11')

    def encrypt():
        message = message_input.get(1.0, END)
        message = str(message.lower())
        message = message[:-1]
        message_buffer = ''
        keyword = keyword_input.get(1.0, END)
        keyword = keyword.lower()
        alphabet = r'абвгдежзийклмнопрстуфхцчшщъыьэюяbdfghijklmnqrstuvwz .,;:!?&%-+="@/\()[]0123456789'
        combined = (str(keyword[:-1]) + str(alphabet))
        alphabet = ''
        coordinates = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "23", "24", "25", "26", "27", "28", "29", "31", "32", "33", "34", "35", "36", "37", "38", "39",
                       "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "52", "53", "54", "55", "56", "57", "58", "59", "61", "62", "63", "64", "65", "66", "67", "68", "69",
                       "71", "72", "73", "74", "75", "76", "77", "78", "79", "81", "82", "83", "84", "85", "86", "87", "88", "89", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
        first_coords, second_coords = "", ""

        result = str("")
        special_chars, special_positions = [], []

        for i in range(len(combined)):
            if alphabet.find(combined[i]) == -1:
                alphabet += combined[i]

        message = message.replace("\n", ' ')
        message = message.replace("ё", 'е')
        message = message.replace("a", 'а')
        message = message.replace("c", 'с')
        message = message.replace("e", 'е')
        message = message.replace("o", 'о')
        message = message.replace("p", 'р')
        message = message.replace("x", 'х')
        message = message.replace("y", 'у')

        while message[len(message) - 1] == " ":
            message = message[:-1]

        count = 0

        for char in message:

            position = alphabet.find(char)

            if char in alphabet:
                message_buffer += coordinates[position]

            else:
                special_chars += [char]
                special_positions += [count - len(special_positions)]

            count += 1

        for i in range(0, len(message_buffer), 2):
            first_coords += message_buffer[i]
        for i in range(1, len(message_buffer), 2):
            second_coords += message_buffer[i]

        message = first_coords + second_coords

        for i in range(0, len(message), 2):
            result += alphabet[coordinates.index(str(message[i] + message[i + 1]))]

        result_buffer = ""
        count = 0

        if special_positions != []:

            for i in range(0, len(result)):

                if i == special_positions[count]:

                    result_buffer = result_buffer + special_chars[count] + result[i]

                    if count < len(special_positions) - 1:
                        count += 1

                else:
                    result_buffer += result[i]

            result = result_buffer

        output.insert(1.0, result + "\n\n")

    def decrypt():
        message = message_input.get(1.0, END)
        message = str(message.lower())
        message_buffer = ''
        keyword = keyword_input.get(1.0, END)
        keyword = keyword.lower()
        alphabet = r'абвгдежзийклмнопрстуфхцчшщъыьэюяbdfghijklmnqrstuvwz .,;:!?&%-+="@/\()[]0123456789'
        combined = (str(keyword[:-1]) + str(alphabet))
        alphabet = ''
        coordinates = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "23", "24", "25", "26", "27", "28", "29", "31", "32", "33", "34", "35", "36", "37", "38", "39",
                       "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "52", "53", "54", "55", "56", "57", "58", "59", "61", "62", "63", "64", "65", "66", "67", "68", "69",
                       "71", "72", "73", "74", "75", "76", "77", "78", "79", "81", "82", "83", "84", "85", "86", "87", "88", "89", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
        first_coords, second_coords = "", ""
        result = str("")
        special_chars = []
        special_positions = []
        message = message.replace("\n", ' ')
        message = message.replace("ё", 'е')
        message = message.replace("a", 'а')
        message = message.replace("c", 'с')
        message = message.replace("e", 'е')
        message = message.replace("o", 'о')
        message = message.replace("p", 'р')
        message = message.replace("x", 'х')
        message = message.replace("y", 'у')

        message = message[:-1]
        while message[len(message) - 1] == " ":
            message = message[:-1]

        for i in range(len(combined)):
            if alphabet.find(combined[i]) == -1:
                alphabet += combined[i]

        count = 0

        for char in message:
            position = alphabet.find(char)

            if char in alphabet:
                message_buffer += coordinates[position]

            else:

                special_chars += [char]
                special_positions += [count - len(special_positions)]

            count += 1

        half = len(message_buffer) // 2
        first_coords = (message_buffer[:half])
        second_coords = (message_buffer[half:])
        interleaved = ""
        for i in range(0, half):
            interleaved = interleaved + first_coords[i] + second_coords[i]

        message = message_buffer

        for i in range(0, len(interleaved), 2):
            result += alphabet[coordinates.index(str(interleaved[i] + interleaved[i + 1]))]

        result_buffer = ''
        count = 0
        if special_positions != []:
            for i in range(0, len(result)):

                if i == special_positions[count]:

                    result_buffer = result_buffer + special_chars[count] + result[i]

                    if count < len(special_positions) - 1:
                        count += 1

                else:
                    result_buffer += result[i]

            result = result_buffer

        output.insert(1.0, result + "\n\n")

    polybius_root = Tk()
    polybius_root.title("ШИФРОВАЛЬЩИК - МЕТОД ПОЛИБИЯ")
    polybius_root.geometry("800x800")
    polybius_root.minsize(width=800, height=800)
    polybius_root.maxsize(width=800, height=800)

    top_frame = Frame(polybius_root, width=190, height=130, bd=5, bg="cyan2")
    top_frame.pack()

    keyword_label = Label(top_frame, fg="pale goldenrod", text="Введите кодовое слово", bg="black", width=100, font="Verdana 15")
    keyword_label.pack()

    keyword_input = Text(top_frame, width=100, fg="yellow", font="Verdana 15", bg="black", height=1)
    keyword_input.pack()

    message_label = Label(top_frame, fg="pale goldenrod", text="Введите сообщение", bg="black", width=70, font="Verdana 15")
    message_label.pack()

    message_input = Text(top_frame, height=9, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    message_input.pack()

    buttons_frame = Frame(polybius_root, width=190, height=100, bd=5, bg="cyan2")
    buttons_frame.pack()

    encrypt_button = Button(buttons_frame, command=encrypt, text="Зашифровать", fg="yellow", font="Verdana 15", width=30, height=2, bg="grey11")
    encrypt_button.grid(row=0, column=0)

    decrypt_button = Button(buttons_frame, command=decrypt, text="Расшифровать", fg="yellow", font="Verdana 15", width=29, height=2, bg="grey11")
    decrypt_button.grid(row=0, column=1)

    output_frame = Frame(polybius_root, width=190, height=130, bd=5, bg="cyan2")
    output_frame.pack()

    output = Text(output_frame, height=12, width=50, fg="azure", font="Verdana 20", bg="black", wrap="word")
    output.pack()

    help_button = Button(top_frame, command=show_polybius_help, text="i", fg="yellow", font="Verdana 15", bg="grey11", width=2, height=1)
    help_button.place(x=749, y=5)
    help_button.bind('<Enter>', darken_help_button)
    help_button.bind('<Leave>', lighten_help_button)

    polybius_root.mainloop()


def highlight_caesar(event):
    event.widget.config(bg='blue2')


def unhighlight_caesar(event):
    event.widget.config(bg='grey11')


def highlight_atbash(event):
    event.widget.config(bg='gold', fg="black")


def unhighlight_atbash(event):
    event.widget.config(bg='grey11', fg="yellow")


def highlight_vigenere(event):
    event.widget.config(bg='red3')


def unhighlight_vigenere(event):
    event.widget.config(bg='grey11')


def highlight_playfair(event):
    event.widget.config(bg='purple')


def unhighlight_playfair(event):
    event.widget.config(bg='grey11')


def highlight_polybius(event):
    event.widget.config(bg='grey')


def unhighlight_polybius(event):
    event.widget.config(bg='grey11')


def highlight_info(event):
    event.widget.config(bg='grey20')


def unhighlight_info(event):
    event.widget.config(bg='grey11')


root = Tk()
root.title("ШИФРОВАЛЬЩИК")
root.geometry("800x700")
root.minsize(width=800, height=700)
root.maxsize(width=800, height=700)
root["bg"] = "cyan2"

main_frame = Frame(root, width=780, height=680, bd=5, bg="black")
main_frame.place(x=10, y=10)

caesar_button = Button(main_frame, text="Сдвиг Цезаря", command=caesar_cipher, fg="yellow", font="Verdana 15", width=17, height=2, bg="grey11")
caesar_button.place(x=10, y=30)
caesar_button.bind('<Enter>', highlight_caesar)
caesar_button.bind('<Leave>', unhighlight_caesar)

atbash_button = Button(main_frame, text="Шифр Атбаш", command=atbash_cipher, fg="yellow", font="Verdana 15", width=17, height=2, bg="grey11")
atbash_button.place(x=10, y=160)
atbash_button.bind('<Enter>', highlight_atbash)
atbash_button.bind('<Leave>', unhighlight_atbash)

vigenere_button = Button(main_frame, text="Шифр Виженера", command=vigenere_cipher, fg="yellow", font="Verdana 15", width=17, height=2, bg="grey11")
vigenere_button.place(x=10, y=290)
vigenere_button.bind('<Enter>', highlight_vigenere)
vigenere_button.bind('<Leave>', unhighlight_vigenere)

playfair_button = Button(main_frame, text="Квадрат Плейфера", command=playfair_cipher, fg="yellow", font="Verdana 15", width=17, height=2, bg="grey11")
playfair_button.place(x=10, y=420)
playfair_button.bind('<Enter>', highlight_playfair)
playfair_button.bind('<Leave>', unhighlight_playfair)

polybius_button = Button(main_frame, text="Метод Полибия", command=polybius_cipher, fg="yellow", font="Verdana 15", width=17, height=2, bg="grey11")
polybius_button.place(x=10, y=550)
polybius_button.bind('<Enter>', highlight_polybius)
polybius_button.bind('<Leave>', unhighlight_polybius)

caesar_description = Label(main_frame, fg="pale goldenrod", justify=LEFT, text="Шифр простой замены. При шифровании \nкаждый символ заменяется\
 другим, стоящим\nот него в алфавите на k позиций. Прост \nв реализации, но не устойчив к взлому.", bg="black", font="Verdana 15")
caesar_description.place(x=260, y=10)

info_button = Button(main_frame, text="Help", fg="yellow", font="Verdana 15", bg="grey11", width=4, height=1, command=show_info)
info_button.place(x=712, y=-2)
info_button.bind('<Enter>', highlight_info)
info_button.bind('<Leave>', unhighlight_info)

atbash_description = Label(main_frame, fg="pale goldenrod", justify=LEFT, text="Шифр простой замены, использованный \nвпервые для еврейск\
ого алфавита. \nЗамена первой буквы алфавита на последню,\nвторой на предпоследнюю и т.д. Не надежен.", bg="black", font="Verdana 15")
atbash_description.place(x=260, y=140)

vigenere_description = Label(main_frame, fg="pale goldenrod", justify=LEFT, text="Метод многоалфавитной замены с кодовым \nсловом. При шифровании каждая буква \nзаменяется на сим\
вол, стоящий на k позиций\nправее, где k – место буквы в кодовом слове.", bg="black", font="Verdana 15")
vigenere_description.place(x=260, y=270)

playfair_description = Label(main_frame, fg="pale goldenrod", justify=LEFT, text="Криптоустойчивый шифр с использованием \nматрицы и кодового слова. Алгоритм          \nзашифровывает па\
ры символов сообщения\nв зависимости от их положения в матрице.", bg="black", font="Verdana 15")
playfair_description.place(x=260, y=400)

polybius_description = Label(main_frame, fg="pale goldenrod", justify=LEFT, text="Нестандартный шифр с применением матрицы.\nСообщение преобразуется в координаты, \nкоторые записыв\
аются вертикально, а \nсчитываются горизонтально. Криптоустойчив.", bg="black", font="Verdana 15")
polybius_description.place(x=259, y=530)

root.clipboard_append("")


def paste_from_clipboard(event):
    message_input['text'] = root.clipboard_get()


def copy_to_clipboard(event):
    root.clipboard_append[output.get(1.0, END)]


root.bind("<Control-v>", paste_from_clipboard)
root.bind("<Control-c>", copy_to_clipboard)

root.mainloop()
