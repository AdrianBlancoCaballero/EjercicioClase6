# Ejercicio de Clase 6

word = input("Introduzca la/s palabra/s: ")
vowels = ["a", "e", "i", "o", "u"]
v_freq = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letter in word:
    if letter in vowels:
        v_freq[letter] += 1

print("Número de vocales en la palabra", word, ":", v_freq)