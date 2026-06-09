"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

NatGatewayState: TypeAlias = Literal[
    "pending",
    "failed",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "failed",
        "available",
        "deleting",
        "deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "failed",
        "available",
        "deleting",
        "deleted",
    )
)


def to_ec2_query_text(value: NatGatewayState) -> str:
    return value


def from_ec2_query_text(text: str) -> NatGatewayState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NatGatewayState value: {text!r}")
    return cast(NatGatewayState, text)


def serialize_ec2_query(
    value: NatGatewayState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NatGatewayState:
    return from_ec2_query_text(el.text or "")
