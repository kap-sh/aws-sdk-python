"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TransitGatewayState: TypeAlias = Literal[
    "pending",
    "available",
    "modifying",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "modifying",
        "deleting",
        "deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "modifying",
        "deleting",
        "deleted",
    )
)


def to_ec2_query_text(value: TransitGatewayState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TransitGatewayState value: {text!r}")
    return cast(TransitGatewayState, text)


def serialize_ec2_query(
    value: TransitGatewayState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayState:
    return from_ec2_query_text(el.text or "")
