"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6AddressAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

Ipv6AddressAttribute: TypeAlias = Literal[
    "public",
    "private",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Ipv6AddressAttribute) -> str:
    return value


def from_ec2_query_text(text: str) -> Ipv6AddressAttribute:
    return cast(Ipv6AddressAttribute, text)


def serialize_ec2_query(
    value: Ipv6AddressAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Ipv6AddressAttribute:
    return from_ec2_query_text(el.text or "")
