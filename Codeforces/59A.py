word = input()
count = 0
for i in word:
    if i == i.upper():
        count += 1
if count > len(word)//2:
    print(word.upper())
else:
    print(word.lower())