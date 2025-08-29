def main() -> None:
    print("""A function object is a value you can assign to a variable or pass as an
argument. For example, do_twice is a function that takes a function object as
an argument and calls it twice:
def do_twice(f):
    f()
    f()
    
Here's an example that uses do_twice to call a function named print_spam
twice:
def print_spam():
    print('spam')

do_twice(print_spam)

1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a
value, and calls the function twice, passing the value as an argument.
3. Copy the definition of print_twice from earlier in this chapter to your
script.
4. Use the modified version of do_twice to call print_twice twice, passing
'spam' as an argument.
5. Define a new function called do_four that takes a function object and a
value and calls the function four times, passing the value as a parameter.
There should be only two statements in the body of this function, not four.
    """)


def do_twice(f, val) -> None:
    f(val)
    f(val)


def do_four(f, val) -> None:
    do_twice(f, val)
    do_twice(f, val)


def print_twice(s) -> None:
    print(s)
    print(s)


def print_spam() -> None:
    print("spam")


if __name__ == "__main__":
    main()
    print('Function call: do_twice(print_twice, "spam")')
    do_twice(print_twice, "spam")
    print()
    print('Function call: do_four(print, "spam")')
    do_four(print, "spam")
