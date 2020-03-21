import logging
import os
from pathlib import Path
import sys

ROOT_DIR = Path(os.path.abspath(__file__)).parent.parent.parent
DATA_DIR = ROOT_DIR / "data"


log_format = "%(asctime)s %(levelname)s: [%(name)s - %(funcName)s()] %(message)s"
logging.basicConfig(
    format=log_format,
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
formatter = logging.Formatter(log_format)
logger = logging.getLogger("covid")
