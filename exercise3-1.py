def right_justify(s: str) -> None:
    print(
        "Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display."
    )
    print("{' ' * (70 - len(s))}{s}")
    print()
    print(f"{' ' * (70 - len(s))}{s}")
    print()


if __name__ == "__main__":
    right_justify("monty")
