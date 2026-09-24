"""Entrypoint"""


def app():
    """
    Main function that prints a greeting message and returns the sum of 1 and 1.

    This function outputs a simple greeting to the console and computes a basic arithmetic
    operation.

    Returns:
        int: The result of the arithmetic operation (1 + 1), which is 2.
    """
    print("Hello from template!")
    return 1 + 1


def main() -> None:
    """Console script entry point.

    Discards the value returned by `app`, so the process exits with status 0.
    """
    app()


if __name__ == "__main__":
    main()
