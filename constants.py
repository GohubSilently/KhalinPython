from pathlib import Path

BASE_DIR = Path(__file__).parent

# Логирование
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'parser.log'
SIZE_LOG = 10**6
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
START_HANDLER = 'START_HANDLER!'
END_HANDLER = 'END_HANDLER!'
COMMAND_LINE_ARGUMENTS = 'Choose regime - {regime}.'

INPUT_NUMBER = 'Input number: '
INPUT_NAME = 'Input name: '
INPUT_ARRAY = 'Input array of numbers separated by spaces: '
