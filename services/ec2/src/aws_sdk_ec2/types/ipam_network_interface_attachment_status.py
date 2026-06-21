"""Generated from Smithy shape ``com.amazonaws.ec2#IpamNetworkInterfaceAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

IpamNetworkInterfaceAttachmentStatus: TypeAlias = Literal[
    "available",
    "in-use",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamNetworkInterfaceAttachmentStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamNetworkInterfaceAttachmentStatus:
    return cast(IpamNetworkInterfaceAttachmentStatus, text)


def serialize_ec2_query(
    value: IpamNetworkInterfaceAttachmentStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamNetworkInterfaceAttachmentStatus:
    return from_ec2_query_text(el.text or "")
