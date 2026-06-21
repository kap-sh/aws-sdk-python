"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpDnsOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

PublicIpDnsOption: TypeAlias = Literal[
    "public-dual-stack-dns-name",
    "public-ipv4-dns-name",
    "public-ipv6-dns-name",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PublicIpDnsOption) -> str:
    return value


def from_ec2_query_text(text: str) -> PublicIpDnsOption:
    return cast(PublicIpDnsOption, text)


def serialize_ec2_query(
    value: PublicIpDnsOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PublicIpDnsOption:
    return from_ec2_query_text(el.text or "")
