"""Generated from Smithy shape ``com.amazonaws.cloudsearch#SuggesterFuzzyMatching``."""

from typing import Literal, TypeAlias, cast

from capo_cloudsearch._protocol.xml import Element

SuggesterFuzzyMatching: TypeAlias = Literal[
    "none",
    "low",
    "high",
]


# --- awsQuery ser/de ---
def to_query_text(value: SuggesterFuzzyMatching) -> str:
    return value


def from_query_text(text: str) -> SuggesterFuzzyMatching:
    return cast(SuggesterFuzzyMatching, text)


def serialize_query(
    value: SuggesterFuzzyMatching, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SuggesterFuzzyMatching:
    return from_query_text(el.text or "")
