"""Generated from Smithy shape ``com.amazonaws.cloudformation#AccountFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

AccountFilterType: TypeAlias = Literal[
    "NONE",
    "INTERSECTION",
    "DIFFERENCE",
    "UNION",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "INTERSECTION",
        "DIFFERENCE",
        "UNION",
    )
)


def to_query_text(value: AccountFilterType) -> str:
    return value


def from_query_text(text: str) -> AccountFilterType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AccountFilterType value: {text!r}")
    return cast(AccountFilterType, text)


def serialize_query(
    value: AccountFilterType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AccountFilterType:
    return from_query_text(el.text or "")
