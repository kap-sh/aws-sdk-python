"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcPeeringConnectionOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.peering_connection_options_request
    import aws_sdk_ec2.types.vpc_peering_connection_id


class ModifyVpcPeeringConnectionOptionsRequest(TypedDict):
    accepter_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options_request.PeeringConnectionOptionsRequest"
    ]
    """<p>The VPC peering connection options for the accepter VPC.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    requester_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options_request.PeeringConnectionOptionsRequest"
    ]
    """<p>The VPC peering connection options for the requester VPC.</p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_id.VpcPeeringConnectionId"
    ]
    """<p>The ID of the VPC peering connection.</p>"""
