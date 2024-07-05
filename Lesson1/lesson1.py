def isValidString(s):
    state = 1
    for char in s:
        if state == 1:
            if char.isupper():
                state = 2
            elif char.islower() or char == " ":
                state = 3
            else:
                return False
        elif state == 2:
            if char.isupper():
                state = 2
            elif char.islower() or char == " ":
                state = 3
            elif char == ".":
                state = 4
            else:
                return False
        elif state == 3:
            if char.islower() or char == " ":
                state = 3
            elif char == ".":
                state = 4
            else:
                return False
        elif state == 4:
            return False
    return state == 4
if __name__ == "__main__":
    print(isValidString("Hello world."))  # True
    print(isValidString("hello world."))  # False
    print(isValidString("Hello world!"))  # False
    print(isValidString("H."))            # True
    print(isValidString("Hello World."))  # True
    print(isValidString("A quick brown fox jumps over the lazy dog."))  # True