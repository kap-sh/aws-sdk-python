"""Generated from Smithy shape ``com.amazonaws.ec2#EventCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

EventCode: TypeAlias = Literal[
    "instance-reboot",
    "system-reboot",
    "system-maintenance",
    "instance-retirement",
    "instance-stop",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "instance-reboot",
        "system-reboot",
        "system-maintenance",
        "instance-retirement",
        "instance-stop",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "instance-reboot",
        "system-reboot",
        "system-maintenance",
        "instance-retirement",
        "instance-stop",
    )
)


def to_ec2_query_text(value: EventCode) -> str:
    return value


def from_ec2_query_text(text: str) -> EventCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EventCode value: {text!r}")
    return cast(EventCode, text)


def serialize_ec2_query(
    value: EventCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EventCode:
    return from_ec2_query_text(el.text or "")
