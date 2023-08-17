# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# Function to translate text to Morse code
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char == ' ':
            morse_code.append(' ')
        else:
            morse_code.append(MORSE_CODE_DICT.get(char, char))
    return ' '.join(morse_code)

# Function to translate Morse code to text
def morse_to_text(morse):
    morse_list = morse.split(' ')
    text = []
    for code in morse_list:
        if code == '':
            text.append(' ')
        else:
            text.append(next((char for char, value in MORSE_CODE_DICT.items() if value == code), code))
    return ''.join(text)

# Main program
choice = input("Choose an option (1: Text to Morse, 2: Morse to Text): ")

if choice == '1':
    text = input("Enter the text to translate to Morse code: ")
    morse = text_to_morse(text)
    print("Morse code:", morse)
elif choice == '2':
    morse = input("Enter the Morse code to translate to text: ")
    text = morse_to_text(morse)
    print("Text:", text)
else:
    print("Invalid choice. Please choose 1 or 2.")
