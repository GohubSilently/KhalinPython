import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import LOG_DIR, LOG_FILE, LOG_FORMAT, DT_FORMAT, SIZE_LOG


def configure_parser():
    parser = argparse.ArgumentParser(
        allow_abbrev=False, description="Interactive output"
    )
    parser.add_argument(
        '-r', '--regime',
        type=int,
        choices=[1, 2, 3],
        required=True,
        help="Choose regime to check",
    )
    return parser


def configure_logging():
    LOG_DIR.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=SIZE_LOG, backupCount=5, encoding="utf-8"
    )
    logging.basicConfig(
        level=logging.INFO,
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        encoding="utf-8",
        handlers=(rotating_handler, logging.StreamHandler()),
    )
