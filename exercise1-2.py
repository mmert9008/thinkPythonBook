def main() -> None:
    print("How many seconds are there in 42 minutes 42 seconds?")
    print("42 * 60 + 42")
    print(f"{42 * 60 + 42} seconds")
    print()
    print(
        "How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile."
    )
    print("10 / 1.61")
    print(f"{round(10 / 1.61, 2)} miles")
    print()
    print(
        "If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?"
    )
    print("(42 * 60 + 42) / (10 / 1.61) // 60 and (42 * 60 + 42) / (10 / 1.61) % 60")
    print(
        f"{int((42 * 60 + 42) / (10 / 1.61) // 60)} minutes and {int(round((42 * 60 + 42) / (10 / 1.61) % 60))} seconds per mile"
    )
    print()
    print("(10 / 1.61) / ((42 * 60 + 42) / 3600)")
    print(f"{round((10 / 1.61) / ((42 * 60 + 42) / 3600), 2)} miles per hour")
    print()


if __name__ == "__main__":
    main()
