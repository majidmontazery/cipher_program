logo = ("""
  ____                              _       
 / ___|__ _ _ __ __ _ _ __ ___   __| | ___  
| |   / _` | '__/ _` | '_ ` _ \ / _` |/ _ \ 
| |__| (_| | | | (_| | | | | | | (_| |  __/ 
 \____\__,_|_|  \__,_|_| |_| |_|\__,_|\___| 

         Caesar Cipher
""")

# Simplified alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Print the logo
print(logo)

# Caesar cipher function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1  # Reverse the shift for decoding

    for char in start_text:
        if char.isalpha():  # Only process alphabetic characters
            is_upper = char.isupper()
            char = char.lower()
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            new_char = alphabet[new_position]
            end_text += new_char.upper() if is_upper else new_char
        else:
            end_text += char  # Keep non-alphabetic characters as they are

    print(f"The {cipher_direction}d result: {end_text}")

# Main program loop
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    
    # Dynamically calculate shift based on text length
    shift = len(text) % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye!")
