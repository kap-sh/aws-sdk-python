"""Generated from Smithy shape ``com.amazonaws.ec2#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

EventType: TypeAlias = Literal[
    "instanceChange",
    "fleetRequestChange",
    "error",
    "information",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "instanceChange",
        "fleetRequestChange",
        "error",
        "information",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "instanceChange",
        "fleetRequestChange",
        "error",
        "information",
    )
)


def to_ec2_query_text(value: EventType) -> str:
    return value


def from_ec2_query_text(text: str) -> EventType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {text!r}")
    return cast(EventType, text)


def serialize_ec2_query(
    value: EventType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EventType:
    return from_ec2_query_text(el.text or "")
