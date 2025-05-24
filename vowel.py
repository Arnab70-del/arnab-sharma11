def check_vowel_or_consonant(char):
    vowels = 'aeiou'
    if char.lower() in vowels:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")


letter = input("Enter a single alphabet character: ")
if letter.isalpha() and len(letter) == 1:
    check_vowel_or_consonant(letter)
else:
    print("Please enter a single alphabet character.")
