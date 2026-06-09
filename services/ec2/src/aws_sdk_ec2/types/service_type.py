"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ServiceType: TypeAlias = Literal[
    "Interface",
    "Gateway",
    "GatewayLoadBalancer",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Interface",
        "Gateway",
        "GatewayLoadBalancer",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "Interface",
        "Gateway",
        "GatewayLoadBalancer",
    )
)


def to_ec2_query_text(value: ServiceType) -> str:
    return value


def from_ec2_query_text(text: str) -> ServiceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceType value: {text!r}")
    return cast(ServiceType, text)


def serialize_ec2_query(
    value: ServiceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ServiceType:
    return from_ec2_query_text(el.text or "")
