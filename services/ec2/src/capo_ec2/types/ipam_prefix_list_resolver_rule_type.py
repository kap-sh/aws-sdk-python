"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamPrefixListResolverRuleType: TypeAlias = Literal[
    "static-cidr",
    "ipam-resource-cidr",
    "ipam-pool-cidr",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamPrefixListResolverRuleType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPrefixListResolverRuleType:
    return cast(IpamPrefixListResolverRuleType, text)


def serialize_ec2_query(
    value: IpamPrefixListResolverRuleType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleType:
    return from_ec2_query_text(el.text or "")
