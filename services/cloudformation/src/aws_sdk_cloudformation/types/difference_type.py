"""Generated from Smithy shape ``com.amazonaws.cloudformation#DifferenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

DifferenceType: TypeAlias = Literal[
    "ADD",
    "REMOVE",
    "NOT_EQUAL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "REMOVE",
        "NOT_EQUAL",
    )
)


def to_query_text(value: DifferenceType) -> str:
    return value


def from_query_text(text: str) -> DifferenceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DifferenceType value: {text!r}")
    return cast(DifferenceType, text)


def serialize_query(
    value: DifferenceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DifferenceType:
    return from_query_text(el.text or "")
