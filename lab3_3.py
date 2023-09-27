t = str(input("Введіть текст: "))

for word in t.split(' '):
    if word.endswith("ий"):
      print(word);