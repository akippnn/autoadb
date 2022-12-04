import sys
import subprocess
import cmd


def iscommand(command: str) -> bool:
    if (command[:2] == '__' and command[-2:]):
        return False
    return True

COMMANDS: list[str] = [command for command in dir(cmd) if iscommand(command)]


def var(key: str, value): 
    VARIABLES[key] = value

VARIABLES: dict = {}


def process(command: str) -> int:
    parse: list = command.split()

    # layer 1 - check if the command exists in cmd
    if command in COMMANDS:
        getattr(cmd, command)()


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
