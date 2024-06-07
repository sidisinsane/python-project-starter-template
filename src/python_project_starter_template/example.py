from python_project_starter_template.logger import log


def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    return a + b


class ExampleClass:
    def method(self, x: int) -> int:
        if not isinstance(x, int):
            raise TypeError("Argument must be integer.")
        return x * 2


EXAMPLE_CONSTANT: int = 42


def main():
    log.info(add(1, 2))

    obj = ExampleClass()
    log.info(obj.method(3))


if __name__ == "__main__":
    main()
