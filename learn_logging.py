from loguru import logger

logger.add("my_log_file.log", rotation="10 MB")


def take_name():
    name = input('Enter name: ')
    return name


def take_sex():
    sex = input('Enter M for male and F for female: ')
    return sex


def take_age():
    age = int(input('Enter age: '))
    return age


def categories(name, sex, age):
    if 13 > age >= 1:
        logger.info(f'{name} is a child')
    elif 19 > age >= 13:
        logger.info(f'{name} is a teenager')
    elif 30 > age >= 19 and sex == 'M':
        logger.info(f'{name} is in his prime')
    elif 30 > age >= 19 and sex == 'F':
        logger.info(f'{name} is in her prime')
    elif 60 > age >= 30:
        logger.info(f'{name} is experienced')
    elif 100 > age >= 60:
        logger.info(f'{name} is a senior person')
    elif age >= 100:
        logger.info(f'{name} is a legend')
    else:
        logger.error('Invalid input')


@logger.catch
def main():
    categories(name=take_name(), sex=take_sex(), age=take_age())


if __name__ == "__main__":
    main()