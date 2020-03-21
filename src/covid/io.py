import json
from pathlib import Path
from typing import List

from covid import DATA_DIR, logger
from covid.structs import Paper


def read_data(path: Path) -> List[Paper]:
    corpus = []
    for file in path.glob("*.json"):
        paper = Paper(**(json.load(open(file, 'rb'))))
        corpus.append(paper)
    logger.info(f"Read {corpus} files from {path}.")
    return corpus


if __name__ == '__main__':

    biorxiv_dir: Path = DATA_DIR / "CORD/2020-03-13/biorxiv_medrxiv/biorxiv_medrxiv/"
    corpus = read_data(biorxiv_dir)

    for paper in corpus:
        print(paper)
