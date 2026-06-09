"""Generated from Smithy shape ``com.amazonaws.ec2#ListingState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ListingState: TypeAlias = Literal[
    "available",
    "sold",
    "cancelled",
    "pending",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "sold",
        "cancelled",
        "pending",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "sold",
        "cancelled",
        "pending",
    )
)


def to_ec2_query_text(value: ListingState) -> str:
    return value


def from_ec2_query_text(text: str) -> ListingState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ListingState value: {text!r}")
    return cast(ListingState, text)


def serialize_ec2_query(
    value: ListingState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ListingState:
    return from_ec2_query_text(el.text or "")
