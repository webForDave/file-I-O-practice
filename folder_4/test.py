# read from file and return alongisde line number
with open('text.txt', 'r') as f:
    for index, content in enumerate(f.readlines(), start=1):
        print(f'{index}: {content}', end="")