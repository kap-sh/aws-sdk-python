"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamResourceType: TypeAlias = Literal[
    "vpc",
    "subnet",
    "eip",
    "public-ipv4-pool",
    "ipv6-pool",
    "eni",
    "anycast-ip-list",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "vpc",
        "subnet",
        "eip",
        "public-ipv4-pool",
        "ipv6-pool",
        "eni",
        "anycast-ip-list",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "vpc",
        "subnet",
        "eip",
        "public-ipv4-pool",
        "ipv6-pool",
        "eni",
        "anycast-ip-list",
    )
)


def to_ec2_query_text(value: IpamResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamResourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamResourceType value: {text!r}")
    return cast(IpamResourceType, text)


def serialize_ec2_query(
    value: IpamResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamResourceType:
    return from_ec2_query_text(el.text or "")
