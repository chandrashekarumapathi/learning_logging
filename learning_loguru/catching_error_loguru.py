from loguru import logger

my_list = [1, 2, 3]
my_variable = {
    'a': 'b'
}


def function_with_error(x, y):
    z = x + y
    return z


@logger.catch
def main():
    while True:
        function_with_error(my_list, my_variable)


if __name__ == "__main__":
    main()
