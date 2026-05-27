"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayVpcAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_subnet_id_list


class ModifyTransitGatewayVpcAttachmentRequest(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    add_subnet_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of one or more subnets to add. You can specify at most one subnet per Availability Zone.</p>"""
    remove_subnet_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of one or more subnets to remove.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options.ModifyTransitGatewayVpcAttachmentRequestOptions"
    ]
    """<p>The new VPC attachment options.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
