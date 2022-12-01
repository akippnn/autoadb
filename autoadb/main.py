import sys
import subprocess
import cmd
VARIABLES: dict = {}


def var(key: str, value): 
    VARIABLES[key] = value


def command(cmd: str) -> int:
    parse: list = cmd.split()

    # layer 1 - check


    result = subprocess.run(parse, stdout = sys.stdout)
    if result.returncode != 0:
        return 1
    else:
        return 0


def main() -> int:
    repr('test')
    result: int

    with open('commands.txt', 'r') as cmds:
        for cmd in cmds:
            result = command(cmd)
            if result:
                return 1

            print("\n", end = "")

    return 0

if __name__ == "__main__":
    main()
