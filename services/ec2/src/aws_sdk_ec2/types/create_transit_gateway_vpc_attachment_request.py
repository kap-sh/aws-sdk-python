"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayVpcAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.transit_gateway_subnet_id_list
    import aws_sdk_ec2.types.vpc_id


class CreateTransitGatewayVpcAttachmentRequest(TypedDict):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one subnet, but we recommend that you specify two subnets for better availability. The transit gateway uses one IP address from each specified subnet.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options.CreateTransitGatewayVpcAttachmentRequestOptions"
    ]
    """<p>The VPC attachment options.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the VPC attachment.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
