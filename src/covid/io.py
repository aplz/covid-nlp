import json
from pathlib import Path
from typing import List

from dacite import from_dict

from covid import logger
from covid.structs import Paper


def read_data(path: Path, limit: int = 0) -> List[Paper]:
    """Import raw data into a list of paper objects.

    Args:
        path: the path to the raw data.
        limit: upper bound on the number of papers to import.

    Returns:
        the list of imported papers.
    """
    corpus = []
    for file in path.glob("**/*.json"):
        dict_ = json.load(open(file.as_posix(), 'rb'))
        paper = from_dict(data_class=Paper, data=dict_)
        corpus.append(paper)
        if 0 < limit <= len(corpus):
            break
    logger.info(f"Read {len(corpus)} files from {path}.")
    return corpus
