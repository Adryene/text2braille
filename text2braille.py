# Braille Grade 1 Alphabet
alphabet_to_braille = {
    'A': '⠠⠁',
    'B': '⠠⠃',
    'C': '⠠⠉',
    'D': '⠠⠙',
    'E': '⠠⠑',
    'F': '⠠⠋',
    'G': '⠠⠛',
    'H': '⠠⠓',
    'I': '⠠⠊',
    'J': '⠠⠚',
    'K': '⠠⠅',
    'L': '⠠⠇',
    'M': '⠠⠍',
    'N': '⠠⠝',
    'O': '⠠⠕',
    'P': '⠠⠏',
    'Q': '⠠⠟',
    'R': '⠠⠗',
    'S': '⠠⠎',
    'T': '⠠⠞',
    'U': '⠠⠥',
    'V': '⠠⠧',
    'W': '⠠⠺',
    'X': '⠠⠭',
    'Y': '⠠⠽',
    'Z': '⠠⠵',
    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
    'k': '⠅',
    'l': '⠇',
    'm': '⠍',
    'n': '⠝',
    'o': '⠕',
    'p': '⠏',
    'q': '⠟',
    'r': '⠗',
    's': '⠎',
    't': '⠞',
    'u': '⠥',
    'v': '⠧',
    'w': '⠺',
    'x': '⠭',
    'y': '⠽',
    'z': '⠵',
    ' ': '⠀',
    '.': '⠲',
    ',': '⠂',
    ';': '⠆',
    ':': '⠒',
    '!': '⠖',
    '?': '⠦',
    '(': '⠢',
    ')': '⠠',
}

# Function for transcribing user input to Braille
def transcribe(input_string):
    output = ''
    for char in input_string:
        if char.upper() in alphabet_to_braille:
            output += alphabet_to_braille[char.upper()]
        elif char.lower() in alphabet_to_braille:
            output += alphabet_to_braille[char.lower()]
    return output

# Get user input
input_string = input('Input text: ')
transcribed = transcribe(input_string)
print(transcribed)

# Save the output to a .txt file
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(transcribed)
