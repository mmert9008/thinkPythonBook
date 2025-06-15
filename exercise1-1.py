def main() -> None:
    print(
        "1. In a print statement, what happens if you leave out one of the parentheses, or both?"
    )
    print("SyntaxError: Missing parentheses in call to 'print'.")
    print()
    print(
        "2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?"
    )
    print("SyntaxError: unterminated string literal")
    print()
    print(
        "3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?"
    )
    print("It is treated as a standard positive integer, 2++2 = 4")
    print()
    print(
        "4. In math notation, leading zeros are okay, as in 02. What happens if you try this in Python?"
    )
    print(
        "SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers"
    )
    print()
    print("5. What happens if you have two values with no operator between them?")
    print("SyntaxError: invalid syntax")
    print()


if __name__ == "__main__":
    main()
