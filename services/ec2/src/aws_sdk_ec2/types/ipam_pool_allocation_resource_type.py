"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAllocationResourceType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpamPoolAllocationResourceType: TypeAlias = Literal[
    "ipam-pool",
    "vpc",
    "ec2-public-ipv4-pool",
    "custom",
    "subnet",
    "eip",
    "anycast-ip-list",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipam-pool",
        "vpc",
        "ec2-public-ipv4-pool",
        "custom",
        "subnet",
        "eip",
        "anycast-ip-list",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ipam-pool",
        "vpc",
        "ec2-public-ipv4-pool",
        "custom",
        "subnet",
        "eip",
        "anycast-ip-list",
    )
)


def to_ec2_query_text(value: IpamPoolAllocationResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPoolAllocationResourceType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown IpamPoolAllocationResourceType value: {text!r}"
        )
    return cast(IpamPoolAllocationResourceType, text)


def serialize_ec2_query(
    value: IpamPoolAllocationResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPoolAllocationResourceType:
    return from_ec2_query_text(el.text or "")
