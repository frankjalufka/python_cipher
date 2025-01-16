def main():
    command = input("Please enter (e)cryption or (d)ecryption: ")
    
    if command.lower() == 'e':
        text = input("Enter your text to encrypt: ")
        custom_key = input("Enter your encryption key: ")
    elif command.lower() == 'd':
        text = input("Enter your text to decrypt: ")
        custom_key = input("Enter your decryption key: ")
    else:
        print('Please enter an "e" for encryption or a "d" for decryption.')
    

    def vigenere(message, key, direction=1):
        key_index = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final_message = ''

        for char in message.lower():

            # Append any non-letter character to the message
            if not char.isalpha():
                final_message += char
            else:        
                # Find the right key character to encode/decode
                key_char = key[key_index % len(key)]
                key_index += 1

                # Define the offset and the encrypted/decrypted letter
                offset = alphabet.index(key_char)
                index = alphabet.find(char)
                new_index = (index + offset*direction) % len(alphabet)
                final_message += alphabet[new_index]
        
        return final_message

    def encrypt(message, key):
        return vigenere(message, key)
        
    def decrypt(message, key):
        return vigenere(message, key, -1)
    if command.lower() == 'e':
        encryption = encrypt(text, custom_key)
        print(f'\nEncrypted text: {encryption}')
    elif command.lower() == 'd':
        decryption = decrypt(text, custom_key)
        print(f'\nDecrypted text: {decryption}\n')
    else:
        print('Please enter an "e" for encryption or a "d" for decryption.')

if __name__ =="__main__":
    main()