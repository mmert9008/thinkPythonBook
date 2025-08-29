import math


def main() -> None:
    print(
        "The volume of a sphere with radius r is 4/3πr3. What is the volume of a sphere with radius 5?"
    )
    print("(4 / 3) * math.pi * 5**3")
    print((4 / 3) * math.pi * 5**3)
    print()
    print(
        "Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?"
    )
    print("(((24.95 - (24.95 * 0.4)) * 60) + (3 * 1) + (0.75 * 59))")
    print(f"${(((24.95 - (24.95 * 0.4)) * 60) + (3 * 1) + (0.75 * 59)):.2f}")
    print()
    print(
        "If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I get home for breakfast?"
    )
    print("(8 + 15/60) + (3 * (7 + 12/60)) + (8 + 15/60)")
    print(
        f"{(8 + 15 / 60) + (3 * (7 + 12 / 60)) + (8 + 15 / 60)} minutes after 6:52 am, at approximately 7:30 am"
    )
    print()


if __name__ == "__main__":
    main()
