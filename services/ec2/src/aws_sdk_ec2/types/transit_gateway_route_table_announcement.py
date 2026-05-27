"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAnnouncement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_direction
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_id
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_state
    import aws_sdk_ec2.types.transit_gateway_route_table_id


class TransitGatewayRouteTableAnnouncement(TypedDict):
    transit_gateway_route_table_announcement_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_id.TransitGatewayRouteTableAnnouncementId"
    ]
    """<p>The ID of the transit gateway route table announcement.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    core_network_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the core network for the transit gateway route table announcement.</p>"""
    peer_transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the peer transit gateway.</p>"""
    peer_core_network_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the core network ID for the peer.</p>"""
    peering_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the peering attachment.</p>"""
    announcement_direction: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_direction.TransitGatewayRouteTableAnnouncementDirection"
    ]
    """<p>The direction for the route table announcement.</p>"""
    transit_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the transit gateway route table.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_state.TransitGatewayRouteTableAnnouncementState"
    ]
    """<p>The state of the transit gateway announcement.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The timestamp when the transit gateway route table announcement was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The key-value pairs associated with the route table announcement.</p>"""
