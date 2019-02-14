def alphabet_position(letter):
    alphabet ="abcdefghijklmnopqrstuvwxyz" 
    lower_letter = letter.lower()   
    return alphabet.index(lower_letter)

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        a = alphabet_position(char) 
        a = (a + rot) % 26            
        a = (alphabet[a])
        if char.isupper():
            a = a.title()
        return a
    else:
       return char