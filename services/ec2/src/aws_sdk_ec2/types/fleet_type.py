"""Generated from Smithy shape ``com.amazonaws.ec2#FleetType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

FleetType: TypeAlias = Literal[
    "request",
    "maintain",
    "instant",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "request",
        "maintain",
        "instant",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "request",
        "maintain",
        "instant",
    )
)


def to_ec2_query_text(value: FleetType) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FleetType value: {text!r}")
    return cast(FleetType, text)


def serialize_ec2_query(
    value: FleetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetType:
    return from_ec2_query_text(el.text or "")
