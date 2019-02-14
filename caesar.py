from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    new_text = ""
    new_char = 0
    for char in text:
        new_char = rotate_character(char, rot)
        new_text += str(new_char)

    return new_text

def main():
    input_text = input("Enter a sentence: ")
    input_rot = int(input("Enter number of rotations: "))

    print(encrypt(input_text, input_rot))

if __name__ == "__main__":
    main()
