"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VerifiedAccessEndpointType: TypeAlias = Literal[
    "load-balancer",
    "network-interface",
    "rds",
    "cidr",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "load-balancer",
        "network-interface",
        "rds",
        "cidr",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "load-balancer",
        "network-interface",
        "rds",
        "cidr",
    )
)


def to_ec2_query_text(value: VerifiedAccessEndpointType) -> str:
    return value


def from_ec2_query_text(text: str) -> VerifiedAccessEndpointType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown VerifiedAccessEndpointType value: {text!r}"
        )
    return cast(VerifiedAccessEndpointType, text)


def serialize_ec2_query(
    value: VerifiedAccessEndpointType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointType:
    return from_ec2_query_text(el.text or "")
