"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayRouteTableAnnouncementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement


class DeleteTransitGatewayRouteTableAnnouncementResult(TypedDict, closed=True):
    transit_gateway_route_table_announcement: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement.TransitGatewayRouteTableAnnouncement"
    ]
    """<p>Provides details about a deleted transit gateway route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayRouteTableAnnouncementResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_route_table_announcement" in value:
        import aws_sdk_ec2.types.transit_gateway_route_table_announcement

        aws_sdk_ec2.types.transit_gateway_route_table_announcement.serialize_ec2_query(
            value["transit_gateway_route_table_announcement"],
            pairs,
            f"{prefix}.TransitGatewayRouteTableAnnouncement",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteTransitGatewayRouteTableAnnouncementResult:
    out: DeleteTransitGatewayRouteTableAnnouncementResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_announcement = el.find(
        "TransitGatewayRouteTableAnnouncement"
    )
    if child_transit_gateway_route_table_announcement is not None:
        import aws_sdk_ec2.types.transit_gateway_route_table_announcement

        out["transit_gateway_route_table_announcement"] = (
            aws_sdk_ec2.types.transit_gateway_route_table_announcement.deserialize_ec2_query(
                child_transit_gateway_route_table_announcement
            )
        )
    return out
