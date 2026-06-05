"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceCidrIpSource``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpamResourceCidrIpSource: TypeAlias = Literal[
    "amazon",
    "byoip",
    "none",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "amazon",
        "byoip",
        "none",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "amazon",
        "byoip",
        "none",
    )
)


def to_ec2_query_text(value: IpamResourceCidrIpSource) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamResourceCidrIpSource:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamResourceCidrIpSource value: {text!r}")
    return cast(IpamResourceCidrIpSource, text)


def serialize_ec2_query(
    value: IpamResourceCidrIpSource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamResourceCidrIpSource:
    return from_ec2_query_text(el.text or "")
