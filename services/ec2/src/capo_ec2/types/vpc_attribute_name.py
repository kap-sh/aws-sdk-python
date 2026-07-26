"""Generated from Smithy shape ``com.amazonaws.ec2#VpcAttributeName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

VpcAttributeName: TypeAlias = Literal[
    "enableDnsSupport",
    "enableDnsHostnames",
    "enableNetworkAddressUsageMetrics",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VpcAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcAttributeName:
    return cast(VpcAttributeName, text)


def serialize_ec2_query(
    value: VpcAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcAttributeName:
    return from_ec2_query_text(el.text or "")
