# Encryptor-Tkinter

A simple graphical tool for text encryption and decryption, written in Python using the Tkinter library.

![Application Screenshot](https://github.com/user-attachments/assets/73b34e23-01e9-464b-91da-4bf50c28734e)

## ✨ Features

The application supports the following classical encryption methods:

*   **Caesar Cipher** — A simple substitution cipher. Each character is replaced by another one shifted by *k* positions in the alphabet. Easy to implement, but not resistant to cracking.
*   **Atbash Cipher** — A simple substitution cipher, first used for the Hebrew alphabet. The first letter of the alphabet is replaced by the last, the second by the second-to-last, and so on. Not reliable.
*   **Vigenère Cipher** — A polyalphabetic substitution method using a keyword. During encryption, each letter is replaced by a character shifted *k* positions to the right, where *k* is the position of the letter in the keyword.
*   **Playfair Square** — A cryptographically strong cipher using a matrix and a keyword. The algorithm encrypts pairs of characters in the message based on their positions in the matrix.
*   **Polybius Square** — A non-standard cipher using a matrix. The message is converted into coordinates, which are written vertically and read horizontally. Cryptographically strong.

## ⚙️ Requirements

*   Python 3.x
*   Tkinter (usually included in standard Python installations on Windows and macOS. Linux users may need to install it separately, for example: `sudo apt-get install python3-tk`).
