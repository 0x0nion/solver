import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "solver.log")

os.makedirs(LOG_DIR, exist_ok=True)


def setup_logger(name: str = "solver"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Файл с ротацией до 5 файлов по 1 МБ
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
    file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    # Консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger