"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

NetworkInterfaceStatus: TypeAlias = Literal[
    "available",
    "associated",
    "attaching",
    "in-use",
    "detaching",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "associated",
        "attaching",
        "in-use",
        "detaching",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "associated",
        "attaching",
        "in-use",
        "detaching",
    )
)


def to_ec2_query_text(value: NetworkInterfaceStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> NetworkInterfaceStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NetworkInterfaceStatus value: {text!r}")
    return cast(NetworkInterfaceStatus, text)


def serialize_ec2_query(
    value: NetworkInterfaceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NetworkInterfaceStatus:
    return from_ec2_query_text(el.text or "")
