"""Generated from Smithy shape ``com.amazonaws.cloudformation#Replacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

Replacement: TypeAlias = Literal[
    "True",
    "False",
    "Conditional",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "True",
        "False",
        "Conditional",
    )
)


def to_query_text(value: Replacement) -> str:
    return value


def from_query_text(text: str) -> Replacement:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Replacement value: {text!r}")
    return cast(Replacement, text)


def serialize_query(
    value: Replacement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Replacement:
    return from_query_text(el.text or "")
