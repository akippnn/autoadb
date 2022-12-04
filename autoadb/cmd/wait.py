import time
import subprocess


def wait(arg: str) -> int:
    try:
        if arg == 'input':
            input("Press Enter to continue...")
        elif arg == "recovery":
            print("Waiting for recovery...\n")
            subprocess.run(['adb', 'wait-for-recovery'])
            time.sleep(2)
            subprocess.run(['adb', 'wait-for-recovery'])
        else:
            time.sleep(float(arg))
        return 0
    except:
        return 1
