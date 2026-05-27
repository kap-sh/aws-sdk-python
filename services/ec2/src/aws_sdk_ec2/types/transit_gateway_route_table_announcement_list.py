"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAnnouncementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement

TransitGatewayRouteTableAnnouncementList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_route_table_announcement.TransitGatewayRouteTableAnnouncement"
]
