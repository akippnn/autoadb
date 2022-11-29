import os
import sys
import subprocess
currentdir = os.getcwd()
variables: dict

VARIABLES = {}

def var(key: str, value): 
    VARIABLES[key] = value

def command(cmd: str) -> int:
    parse: list = cmd.split()

    # print("[{}] ".format(parse[0] if 'shell' not in parse[1:3] else 'shell'),  end=" ")
    # for item in parse[1:]:
    #     if "wait-for-" in item:
    #         continue
    #     if item == "shell":
    #         continue
    #     print("{}".format(item), end=" ")
    # print("\n", end="")

    # if parse[1] == 'wait-for-recovery':
    #     print("Waiting for recovery to respond...")
    # elif parse[1] == 'wait-for-sideload':
    #     print("Waiting for ADB sideload...")

    
    
    result = subprocess.run(parse, stdout=sys.stdout)
    if result.returncode != 0:
        return 1
    else:
        return 0

def main() -> int:
    repr('test')
    result: int; variables: dict
    os.system('cls' if os.name == 'nt' else 'clear')

    with open('commands.txt', 'r') as cmds:
        for cmd in cmds:
            result = command(cmd)
            if result:
                return 1

            print("\n", end="")

    return 0

if __name__ == "__main__":
    main()
