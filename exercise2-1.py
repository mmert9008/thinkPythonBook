def main() -> None:
    print("We've seen that n = 42 is legal. What about 42 = n?")
    print(
        "SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?"
    )
    print()
    print("How about x = y = 1?")
    print("It is legal, 1 is assigned to both x and y")
    print()
    print(
        "In some languages every statement ends with a semicolon, ;. What happens if you put a semicolon at the end of a Python statement?"
    )
    print("Nothing happens, the statement is evaluated as normal")
    print()
    print("What if you put a period at the end of a statement?")
    print("SyntaxError: invalid syntax")
    print()
    print(
        "In math notation you can multiply x and y like this: xy. What happens if you try that in Python?"
    )
    print("NameError: name 'xy' is not defined. Did you mean: 'x'?")
    print()


if __name__ == "__main__":
    main()
