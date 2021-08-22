# check loop string
def check(child, parent):
    ratio = len(parent) // len(child)
    if len(parent) % len(child) == 0:
        if child * ratio == parent:
            return True

if __name__ == '__main__':
    my_string = input("Enter a string: ")
    for i in range(1, len(my_string) // 2 + 1):
        if check(my_string[:i],my_string):
            print(f"'{my_string}' is loop string")
            break
    else:
        print(f"'{my_string}' is not loop string")