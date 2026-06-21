"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TransitGatewayRouteState: TypeAlias = Literal[
    "pending",
    "active",
    "blackhole",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayRouteState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayRouteState:
    return cast(TransitGatewayRouteState, text)


def serialize_ec2_query(
    value: TransitGatewayRouteState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteState:
    return from_ec2_query_text(el.text or "")
