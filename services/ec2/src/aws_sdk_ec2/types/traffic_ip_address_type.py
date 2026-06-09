"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficIpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TrafficIpAddressType: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dual-stack",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
        "dual-stack",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
        "dual-stack",
    )
)


def to_ec2_query_text(value: TrafficIpAddressType) -> str:
    return value


def from_ec2_query_text(text: str) -> TrafficIpAddressType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TrafficIpAddressType value: {text!r}")
    return cast(TrafficIpAddressType, text)


def serialize_ec2_query(
    value: TrafficIpAddressType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TrafficIpAddressType:
    return from_ec2_query_text(el.text or "")
