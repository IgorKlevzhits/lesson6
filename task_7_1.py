def counting_number_vowels(phrase):
    number_vowels = 0
    phrase = phrase.upper()
    for letter in phrase:
        if (letter == "А" or letter == "Е" or letter == "Ё" or letter == "И" or letter == "Й" or 
        letter == "О" or letter == "У" or letter == "Ы" or letter == "Э" or letter == "Ю" or letter == "Я"):
            number_vowels += 1
    return number_vowels

print(counting_number_vowels("Арарат-азамат-тахирович"))