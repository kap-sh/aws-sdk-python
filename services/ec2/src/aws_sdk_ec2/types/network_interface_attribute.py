"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceAttribute``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

NetworkInterfaceAttribute: TypeAlias = Literal[
    "description",
    "groupSet",
    "sourceDestCheck",
    "attachment",
    "associatePublicIpAddress",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "description",
        "groupSet",
        "sourceDestCheck",
        "attachment",
        "associatePublicIpAddress",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "description",
        "groupSet",
        "sourceDestCheck",
        "attachment",
        "associatePublicIpAddress",
    )
)


def to_ec2_query_text(value: NetworkInterfaceAttribute) -> str:
    return value


def from_ec2_query_text(text: str) -> NetworkInterfaceAttribute:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NetworkInterfaceAttribute value: {text!r}")
    return cast(NetworkInterfaceAttribute, text)


def serialize_ec2_query(
    value: NetworkInterfaceAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NetworkInterfaceAttribute:
    return from_ec2_query_text(el.text or "")
