"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_attachment_list
    import aws_sdk_ec2.types.transit_gateway_route_state
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_id
    import aws_sdk_ec2.types.transit_gateway_route_type


class TransitGatewayRoute(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list used for destination matches.</p>"""
    transit_gateway_route_table_announcement_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_id.TransitGatewayRouteTableAnnouncementId"
    ]
    """<p>The ID of the transit gateway route table announcement. </p>"""
    transit_gateway_attachments: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_attachment_list.TransitGatewayRouteAttachmentList"
    ]
    """<p>The attachments.</p>"""
    type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_type.TransitGatewayRouteType"
    ]
    """<p>The route type.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_state.TransitGatewayRouteState"
    ]
    """<p>The state of the route.</p>"""
