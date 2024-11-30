with open('text.txt', 'r') as f:
    with open('text_2.txt', 'w') as f1:
        for content in f:
            f1.write(content)