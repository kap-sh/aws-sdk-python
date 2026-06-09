"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TransitGatewayMulticastDomainState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


def to_ec2_query_text(value: TransitGatewayMulticastDomainState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayMulticastDomainState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayMulticastDomainState value: {text!r}"
        )
    return cast(TransitGatewayMulticastDomainState, text)


def serialize_ec2_query(
    value: TransitGatewayMulticastDomainState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastDomainState:
    return from_ec2_query_text(el.text or "")
