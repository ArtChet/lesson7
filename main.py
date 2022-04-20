pals = ('Stromae', 'abccba', 'мадам', '1323453', 'шалаш', 'eight')

palindromes = tuple(filter(lambda words: words == words[::-1], pals))

print(palindromes)