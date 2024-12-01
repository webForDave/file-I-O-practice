import sys

def main():
    return count_lines()
 
def count_lines():
    if len(sys.argv) > 2:
        sys.exit('Too many commandline arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        if sys.argv[1].endswith('.py'):
            try:
                with open(sys.argv[1]) as file:
                    lines = [line.strip() for line in file]
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a python file')
    
    lines = [line for line in lines if not(line.startswith('#') or line == '')]
    return len(lines)

if __name__ == '__main__':
    print(main())