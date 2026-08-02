"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayRouteTableAnnouncementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_route_table_announcement


class CreateTransitGatewayRouteTableAnnouncementResult(TypedDict, closed=True):
    transit_gateway_route_table_announcement: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_announcement.TransitGatewayRouteTableAnnouncement"
    ]
    """<p>Provides details about the transit gateway route table announcement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayRouteTableAnnouncementResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_route_table_announcement" in value:
        import capo_ec2.types.transit_gateway_route_table_announcement

        capo_ec2.types.transit_gateway_route_table_announcement.serialize_ec2_query(
            value["transit_gateway_route_table_announcement"],
            pairs,
            f"{key_prefix}TransitGatewayRouteTableAnnouncement",
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateTransitGatewayRouteTableAnnouncementResult:
    out: CreateTransitGatewayRouteTableAnnouncementResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_announcement = el.find(
        "TransitGatewayRouteTableAnnouncement"
    )
    if child_transit_gateway_route_table_announcement is not None:
        import capo_ec2.types.transit_gateway_route_table_announcement

        out["transit_gateway_route_table_announcement"] = (
            capo_ec2.types.transit_gateway_route_table_announcement.deserialize_ec2_query(
                child_transit_gateway_route_table_announcement
            )
        )
    return out
