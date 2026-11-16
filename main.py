import logging
from typing import Iterable, List

from configs import configure_logging, configure_parser
from constants import (
    START_HANDLER, COMMAND_LINE_ARGUMENTS,
    INPUT_NAME, INPUT_NUMBER, INPUT_ARRAY,
    END_HANDLER,
)


def _multiplies_three(data: Iterable[int | float]) -> list[int | float]:
    result = []
    for number in data:
        if isinstance(number, bool):
            continue
        if number % 3 == 0:
            result.append(number)
    return result


def main(data: int | float | str | Iterable[int | float]) -> str | List[int | float]:
    if isinstance(data, bool):
        return 'Unsupported type'

    if isinstance(data, (int, float)):
        if data > 7:
            return 'Hello'
        return 'This number is less or equal 7'

    if isinstance(data, str):
        if data.strip().capitalize() == 'John':
            return 'Hello, John'
        return 'There is no such name'

    if isinstance(data, Iterable) and not isinstance(data, dict):
        return _multiplies_three(data)
    return 'Unsupported type'


if __name__ == '__main__':
    configure_logging()
    logging.info(START_HANDLER)
    parser = configure_parser()
    args = parser.parse_args()
    logging.info(COMMAND_LINE_ARGUMENTS.format(**vars(args)))

    data = ''
    if args.regime == 1:
        data = float(input(INPUT_NUMBER))
    elif args.regime == 2:
        data = input(INPUT_NAME)
    elif args.regime == 3:
        data = map(int, input(INPUT_ARRAY).split())

    result = main(data=data)
    print(result)
    logging.info(END_HANDLER)
