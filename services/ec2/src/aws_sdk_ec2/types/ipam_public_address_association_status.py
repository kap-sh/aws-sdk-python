"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

IpamPublicAddressAssociationStatus: TypeAlias = Literal[
    "associated",
    "disassociated",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamPublicAddressAssociationStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPublicAddressAssociationStatus:
    return cast(IpamPublicAddressAssociationStatus, text)


def serialize_ec2_query(
    value: IpamPublicAddressAssociationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPublicAddressAssociationStatus:
    return from_ec2_query_text(el.text or "")
