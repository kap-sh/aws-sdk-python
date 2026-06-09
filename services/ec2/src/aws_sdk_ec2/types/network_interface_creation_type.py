"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceCreationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

NetworkInterfaceCreationType: TypeAlias = Literal[
    "efa",
    "efa-only",
    "branch",
    "trunk",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "efa",
        "efa-only",
        "branch",
        "trunk",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "efa",
        "efa-only",
        "branch",
        "trunk",
    )
)


def to_ec2_query_text(value: NetworkInterfaceCreationType) -> str:
    return value


def from_ec2_query_text(text: str) -> NetworkInterfaceCreationType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown NetworkInterfaceCreationType value: {text!r}"
        )
    return cast(NetworkInterfaceCreationType, text)


def serialize_ec2_query(
    value: NetworkInterfaceCreationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NetworkInterfaceCreationType:
    return from_ec2_query_text(el.text or "")
