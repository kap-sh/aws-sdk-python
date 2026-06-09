"""Generated from Smithy shape ``com.amazonaws.ec2#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
    "ipv6",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
        "ipv6",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
        "ipv6",
    )
)


def to_ec2_query_text(value: IpAddressType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpAddressType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {text!r}")
    return cast(IpAddressType, text)


def serialize_ec2_query(
    value: IpAddressType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpAddressType:
    return from_ec2_query_text(el.text or "")
