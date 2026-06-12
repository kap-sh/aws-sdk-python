"""Generated from Smithy shape ``com.amazonaws.cloudsearch#SuggesterFuzzyMatching``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

SuggesterFuzzyMatching: TypeAlias = Literal[
    "none",
    "low",
    "high",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "low",
        "high",
    )
)


def to_query_text(value: SuggesterFuzzyMatching) -> str:
    return value


def from_query_text(text: str) -> SuggesterFuzzyMatching:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SuggesterFuzzyMatching value: {text!r}")
    return cast(SuggesterFuzzyMatching, text)


def serialize_query(
    value: SuggesterFuzzyMatching, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SuggesterFuzzyMatching:
    return from_query_text(el.text or "")
