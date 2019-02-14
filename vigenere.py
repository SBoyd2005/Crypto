from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    l = []
    keystream = 0
    for i in range(len(text)):
        keychar = keystream % len(rot)
        if text[i].isalpha():
            l.append(rotate_character(text[i], alphabet_position(rot[keychar])))
            keystream += 1
        else:
            l.append(text[i])

    return (''.join(l))

def main():
    input_text = input("Enter a sentence: ")
    input_rot = input("Enter number of rotations: ")

    print(encrypt(input_text, input_rot))

if __name__ == "__main__":
    main()
