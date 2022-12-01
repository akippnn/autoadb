def echo(string: str, dictionary: dict) -> int:
    try:
        if string:
            print(string)
        if dictionary:
            for string in dictionary:
                print("{}".format(string), end=" ")
        return 0

    except:
        return 1
