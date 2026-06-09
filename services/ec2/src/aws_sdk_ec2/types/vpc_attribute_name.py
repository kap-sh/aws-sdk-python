"""Generated from Smithy shape ``com.amazonaws.ec2#VpcAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VpcAttributeName: TypeAlias = Literal[
    "enableDnsSupport",
    "enableDnsHostnames",
    "enableNetworkAddressUsageMetrics",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enableDnsSupport",
        "enableDnsHostnames",
        "enableNetworkAddressUsageMetrics",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enableDnsSupport",
        "enableDnsHostnames",
        "enableNetworkAddressUsageMetrics",
    )
)


def to_ec2_query_text(value: VpcAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcAttributeName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpcAttributeName value: {text!r}")
    return cast(VpcAttributeName, text)


def serialize_ec2_query(
    value: VpcAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcAttributeName:
    return from_ec2_query_text(el.text or "")
