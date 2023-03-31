def counting_number_vowels(phrase):
    number_vowels = 0
    for letter in phrase:
        if (letter == "А" or letter == "Е" or letter == "Ё" or letter == "И" or letter == "Й" or 
        letter == "О" or letter == "У" or letter == "Ы" or letter == "Э" or letter == "Ю" or letter == "Я"):
            number_vowels += 1
    return number_vowels

def check_song(counting_number_vowels, phrases):
    number_vowels = counting_number_vowels(phrases[0])
    for phrase in phrases:
        if number_vowels != counting_number_vowels(phrase):
            return False
    return True

song = input("Введите вашу песню: ").upper().split()
if check_song(counting_number_vowels, song):
    print("Парам пам-пам")
else:
    print("Пам парам")