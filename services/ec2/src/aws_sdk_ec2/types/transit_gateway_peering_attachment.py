"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.peering_attachment_status
    import aws_sdk_ec2.types.peering_tgw_info
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_attachment_state
    import aws_sdk_ec2.types.transit_gateway_peering_attachment_options


class TransitGatewayPeeringAttachment(TypedDict):
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway peering attachment.</p>"""
    accepter_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The ID of the accepter transit gateway attachment.</p>"""
    requester_tgw_info: NotRequired["aws_sdk_ec2.types.peering_tgw_info.PeeringTgwInfo"]
    """<p>Information about the requester transit gateway.</p>"""
    accepter_tgw_info: NotRequired["aws_sdk_ec2.types.peering_tgw_info.PeeringTgwInfo"]
    """<p>Information about the accepter transit gateway.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_peering_attachment_options.TransitGatewayPeeringAttachmentOptions"
    ]
    """<p>Details about the transit gateway peering attachment.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.peering_attachment_status.PeeringAttachmentStatus"
    ]
    """<p>The status of the transit gateway peering attachment.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_state.TransitGatewayAttachmentState"
    ]
    """<p>The state of the transit gateway peering attachment. Note that the <code>initiating</code> state has been deprecated.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time the transit gateway peering attachment was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the transit gateway peering attachment.</p>"""
