"""Generated from Smithy shape ``com.amazonaws.ec2#IpVersionEnum``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpVersionEnum: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpVersionEnum) -> str:
    return value


def from_ec2_query_text(text: str) -> IpVersionEnum:
    return cast(IpVersionEnum, text)


def serialize_ec2_query(
    value: IpVersionEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpVersionEnum:
    return from_ec2_query_text(el.text or "")
