# read and count words
with open('text.txt', 'r') as f:
    content = f.read()
    count = 0

    for word in content:
        if word != '':
            count += 1
print(count)