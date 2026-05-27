"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcPeeringConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.vpc_id


class CreateVpcPeeringConnectionRequest(TypedDict):
    peer_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.</p> <p>Default: The Region in which you make the request.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the peering connection.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the requester VPC. You must specify this parameter in the request.</p>"""
    peer_vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.</p>"""
    peer_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the accepter VPC.</p> <p>Default: Your Amazon Web Services account ID</p>"""
