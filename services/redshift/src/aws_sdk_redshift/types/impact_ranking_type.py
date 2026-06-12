"""Generated from Smithy shape ``com.amazonaws.redshift#ImpactRankingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ImpactRankingType: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "MEDIUM",
        "LOW",
    )
)


def to_query_text(value: ImpactRankingType) -> str:
    return value


def from_query_text(text: str) -> ImpactRankingType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ImpactRankingType value: {text!r}")
    return cast(ImpactRankingType, text)


def serialize_query(
    value: ImpactRankingType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ImpactRankingType:
    return from_query_text(el.text or "")
