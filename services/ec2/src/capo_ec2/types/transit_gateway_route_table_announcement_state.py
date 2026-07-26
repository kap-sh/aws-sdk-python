"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAnnouncementState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayRouteTableAnnouncementState: TypeAlias = Literal[
    "available",
    "pending",
    "failing",
    "failed",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayRouteTableAnnouncementState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayRouteTableAnnouncementState:
    return cast(TransitGatewayRouteTableAnnouncementState, text)


def serialize_ec2_query(
    value: TransitGatewayRouteTableAnnouncementState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableAnnouncementState:
    return from_ec2_query_text(el.text or "")
