"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AvailabilityMode: TypeAlias = Literal[
    "zonal",
    "regional",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "zonal",
        "regional",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "zonal",
        "regional",
    )
)


def to_ec2_query_text(value: AvailabilityMode) -> str:
    return value


def from_ec2_query_text(text: str) -> AvailabilityMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AvailabilityMode value: {text!r}")
    return cast(AvailabilityMode, text)


def serialize_ec2_query(
    value: AvailabilityMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AvailabilityMode:
    return from_ec2_query_text(el.text or "")
