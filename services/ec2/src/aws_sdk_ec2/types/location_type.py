"""Generated from Smithy shape ``com.amazonaws.ec2#LocationType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

LocationType: TypeAlias = Literal[
    "region",
    "availability-zone",
    "availability-zone-id",
    "outpost",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "region",
        "availability-zone",
        "availability-zone-id",
        "outpost",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "region",
        "availability-zone",
        "availability-zone-id",
        "outpost",
    )
)


def to_ec2_query_text(value: LocationType) -> str:
    return value


def from_ec2_query_text(text: str) -> LocationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LocationType value: {text!r}")
    return cast(LocationType, text)


def serialize_ec2_query(
    value: LocationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LocationType:
    return from_ec2_query_text(el.text or "")
