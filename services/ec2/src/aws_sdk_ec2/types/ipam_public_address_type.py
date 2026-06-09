"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamPublicAddressType: TypeAlias = Literal[
    "service-managed-ip",
    "service-managed-byoip",
    "amazon-owned-eip",
    "amazon-owned-contig",
    "byoip",
    "ec2-public-ip",
    "anycast-ip-list-ip",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "service-managed-ip",
        "service-managed-byoip",
        "amazon-owned-eip",
        "amazon-owned-contig",
        "byoip",
        "ec2-public-ip",
        "anycast-ip-list-ip",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "service-managed-ip",
        "service-managed-byoip",
        "amazon-owned-eip",
        "amazon-owned-contig",
        "byoip",
        "ec2-public-ip",
        "anycast-ip-list-ip",
    )
)


def to_ec2_query_text(value: IpamPublicAddressType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPublicAddressType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamPublicAddressType value: {text!r}")
    return cast(IpamPublicAddressType, text)


def serialize_ec2_query(
    value: IpamPublicAddressType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPublicAddressType:
    return from_ec2_query_text(el.text or "")
