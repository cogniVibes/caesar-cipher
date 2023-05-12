# Core encryption/decryption function
def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        result += char

    return result

# Get mode
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        action = 'encrypt'
        break
    elif response.startswith('d'):
        action = 'decrypt'
        break
    print('Please enter the letter e or d.')

print("Enter the message.")
message = input('> ')

# Get shift value
while True:
    maxKey = 26
    print('Please enter the key (0 to 25) to use.')
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < 26:
        key = int(response)
        break

# Perform encryption/decryption
result = caesar_cipher(message, key, action)

# Display the result
print(f"Result: {result}")
