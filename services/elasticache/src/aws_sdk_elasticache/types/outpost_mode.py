"""Generated from Smithy shape ``com.amazonaws.elasticache#OutpostMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

OutpostMode: TypeAlias = Literal[
    "single-outpost",
    "cross-outpost",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "single-outpost",
        "cross-outpost",
    )
)


def to_query_text(value: OutpostMode) -> str:
    return value


def from_query_text(text: str) -> OutpostMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OutpostMode value: {text!r}")
    return cast(OutpostMode, text)


def serialize_query(
    value: OutpostMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OutpostMode:
    return from_query_text(el.text or "")
