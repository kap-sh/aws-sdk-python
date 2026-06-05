"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

TransitGatewayRouteTableState: TypeAlias = Literal[
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


def to_ec2_query_text(value: TransitGatewayRouteTableState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayRouteTableState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayRouteTableState value: {text!r}"
        )
    return cast(TransitGatewayRouteTableState, text)


def serialize_ec2_query(
    value: TransitGatewayRouteTableState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableState:
    return from_ec2_query_text(el.text or "")
