import sys

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
else:
    if not (sys.argv[1].endswith('.csv')):
        sys.exit('Not a CSV file')
    else:
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    print(line, end='')
        except FileNotFoundError:
            sys.exit('File does not exist')