import math
import turtle


def bob_turt() -> None:
    print(bob)
    bob.fd(100)
    bob.lt(90)
    bob.fd(100)
    bob.lt(90)
    bob.fd(100)
    bob.lt(90)
    bob.fd(100)

    for i in range(4):
        bob.fd(100)
        bob.lt(90)


def square(t, length) -> None:
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n) -> None:
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


def circle(t, r) -> None:
    num_sides = 50
    circumference = 2 * math.pi * r
    side_length = circumference / num_sides
    for i in range(num_sides):
        t.fd(side_length)
        t.lt(360 / num_sides)


def arc(t, r, angle) -> None:
    num_steps = max(1, int(50 * (angle / 360.0)))
    circumference = 2 * math.pi * r
    arc_length = circumference * (angle / 360.0)
    side_length = arc_length / num_steps
    turn_angle_per_step = angle / num_steps
    for _ in range(num_steps):
        t.fd(side_length)
        t.lt(turn_angle_per_step)


if __name__ == "__main__":
    bob = turtle.Turtle()
    # bob_turt()
    # square(bob, 25)
    # polygon(bob, 70, 7)
    # circle(bob, 100)
    arc(bob, 100, 180)

    turtle.mainloop()
