"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAnnouncementDirection``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayRouteTableAnnouncementDirection: TypeAlias = Literal[
    "outgoing",
    "incoming",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayRouteTableAnnouncementDirection) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayRouteTableAnnouncementDirection:
    return cast(TransitGatewayRouteTableAnnouncementDirection, text)


def serialize_ec2_query(
    value: TransitGatewayRouteTableAnnouncementDirection,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableAnnouncementDirection:
    return from_ec2_query_text(el.text or "")
