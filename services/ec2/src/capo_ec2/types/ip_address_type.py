"""Generated from Smithy shape ``com.amazonaws.ec2#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
    "ipv6",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpAddressType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpAddressType:
    return cast(IpAddressType, text)


def serialize_ec2_query(
    value: IpAddressType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpAddressType:
    return from_ec2_query_text(el.text or "")
