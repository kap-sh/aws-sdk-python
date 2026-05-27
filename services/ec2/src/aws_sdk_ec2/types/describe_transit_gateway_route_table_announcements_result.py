"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayRouteTableAnnouncementsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_list


class DescribeTransitGatewayRouteTableAnnouncementsResult(TypedDict):
    transit_gateway_route_table_announcements: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_list.TransitGatewayRouteTableAnnouncementList"
    ]
    """<p>Describes the transit gateway route table announcement.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
