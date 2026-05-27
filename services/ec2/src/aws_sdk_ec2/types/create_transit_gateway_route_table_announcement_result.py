"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayRouteTableAnnouncementResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement


class CreateTransitGatewayRouteTableAnnouncementResult(TypedDict):
    transit_gateway_route_table_announcement: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement.TransitGatewayRouteTableAnnouncement"
    ]
    """<p>Provides details about the transit gateway route table announcement.</p>"""
