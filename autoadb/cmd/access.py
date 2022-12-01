import json

def main(self, file: str) -> dict:
    with open(file, 'w') as obj:
        return json.load(obj)
