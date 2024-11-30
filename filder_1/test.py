# write to file
with open('text.txt', 'w') as f:
    for i in range(1, 100+1):
        f.write(f'{i}\n')