"""Generated from Smithy shape ``com.amazonaws.ec2#HostMaintenance``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

HostMaintenance: TypeAlias = Literal[
    "on",
    "off",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "on",
        "off",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "on",
        "off",
    )
)


def to_ec2_query_text(value: HostMaintenance) -> str:
    return value


def from_ec2_query_text(text: str) -> HostMaintenance:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HostMaintenance value: {text!r}")
    return cast(HostMaintenance, text)


def serialize_ec2_query(
    value: HostMaintenance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HostMaintenance:
    return from_ec2_query_text(el.text or "")
