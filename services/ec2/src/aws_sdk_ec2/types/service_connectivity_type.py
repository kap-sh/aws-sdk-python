"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceConnectivityType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ServiceConnectivityType: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
    )
)


def to_ec2_query_text(value: ServiceConnectivityType) -> str:
    return value


def from_ec2_query_text(text: str) -> ServiceConnectivityType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceConnectivityType value: {text!r}")
    return cast(ServiceConnectivityType, text)


def serialize_ec2_query(
    value: ServiceConnectivityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ServiceConnectivityType:
    return from_ec2_query_text(el.text or "")
