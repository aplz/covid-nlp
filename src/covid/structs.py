from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Author:
    first: str = None
    middle: List[str] = field(default_factory=list)
    last: str = None
    suffix: str = None
    affiliation: Dict = field(default_factory=dict)
    email: str = None


@dataclass
class Paragraph:
    text: str = None
    cite_spans: List[Dict] = field(default_factory=list)
    ref_spans: List[Dict] = field(default_factory=list)
    section: str = None


@dataclass
class MetaData:
    title: str = None
    authors: List[Author] = field(default_factory=list)


@dataclass
class Paper:
    paper_id: str = None
    metadata: MetaData = None
    abstract: List[Paragraph] = field(default_factory=list)
    body_text: List[Paragraph] = field(default_factory=list)
    bib_entries: Dict = field(default_factory=dict)
    ref_entries: Dict = field(default_factory=dict)
    back_matter: List[Dict] = field(default_factory=list)
