# Intermediary file
import os
import sys

def main() -> int:
    args = sys.argv[sys.argv.index('start.py') + 1:]
    os.system('cls' if os.name == 'nt' else 'clear')
    return os.system("./adbwrapper/main.py {}".format(" ".join(args)))

if __name__ == "__main__":
    main()
