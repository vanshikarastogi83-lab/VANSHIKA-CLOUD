sentence = "this is a test this is only a test"
words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
for word, count in frequency.items():
    print(word, ":", count)
