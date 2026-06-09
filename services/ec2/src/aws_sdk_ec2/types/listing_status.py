"""Generated from Smithy shape ``com.amazonaws.ec2#ListingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ListingStatus: TypeAlias = Literal[
    "active",
    "pending",
    "cancelled",
    "closed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "pending",
        "cancelled",
        "closed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "pending",
        "cancelled",
        "closed",
    )
)


def to_ec2_query_text(value: ListingStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> ListingStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ListingStatus value: {text!r}")
    return cast(ListingStatus, text)


def serialize_ec2_query(
    value: ListingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ListingStatus:
    return from_ec2_query_text(el.text or "")
