"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayPeeringAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_transit_gateway_peering_attachment_request_options
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_association_gateway_id
    import aws_sdk_ec2.types.transit_gateway_id


class CreateTransitGatewayPeeringAttachmentRequest(TypedDict):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    peer_transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_association_gateway_id.TransitAssociationGatewayId"
    ]
    """<p>The ID of the peer transit gateway with which to create the peering attachment.</p>"""
    peer_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the peer transit gateway.</p>"""
    peer_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region where the peer transit gateway is located.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.create_transit_gateway_peering_attachment_request_options.CreateTransitGatewayPeeringAttachmentRequestOptions"
    ]
    """<p>Requests a transit gateway peering attachment.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the transit gateway peering attachment.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
