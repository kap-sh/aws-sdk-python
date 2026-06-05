"""Generated from Smithy shape ``com.amazonaws.ec2#DnsRecordIpType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

DnsRecordIpType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
    "ipv6",
    "service-defined",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
        "ipv6",
        "service-defined",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
        "ipv6",
        "service-defined",
    )
)


def to_ec2_query_text(value: DnsRecordIpType) -> str:
    return value


def from_ec2_query_text(text: str) -> DnsRecordIpType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DnsRecordIpType value: {text!r}")
    return cast(DnsRecordIpType, text)


def serialize_ec2_query(
    value: DnsRecordIpType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DnsRecordIpType:
    return from_ec2_query_text(el.text or "")
