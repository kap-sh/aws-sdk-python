"""Generated from Smithy shape ``com.amazonaws.ec2#IpamAddressHistoryResourceType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamAddressHistoryResourceType: TypeAlias = Literal[
    "eip",
    "vpc",
    "subnet",
    "network-interface",
    "instance",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamAddressHistoryResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamAddressHistoryResourceType:
    return cast(IpamAddressHistoryResourceType, text)


def serialize_ec2_query(
    value: IpamAddressHistoryResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamAddressHistoryResourceType:
    return from_ec2_query_text(el.text or "")
