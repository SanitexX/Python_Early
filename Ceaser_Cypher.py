alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("Type 'encode' to encrypt and decode to decrypt: \n").lower()
text = input("Type youre message: \n").lower()
shift = int(input("Type shift number: \n"))

# Function to encode or decode
def ceaser(original_text, shift_amount, encode_or_decode):
    cypher = ""
    
    # If decoding, reverse the shift amount by multiplying by -1
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alpha:  # Only shift alphabetic characters
            # Find the shifted position, wrapping around using % 26
            shifted_position = (alpha.index(letter) + shift_amount) % len(alpha)
            cypher += alpha[shifted_position]
        else:
            # If the character is not a letter (space, punctuation), just add it as is
            cypher += letter
    
    # Print the result
    print(f"Here's your {encode_or_decode}d text: {cypher}")

# Correct the order of arguments when calling the function
ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

