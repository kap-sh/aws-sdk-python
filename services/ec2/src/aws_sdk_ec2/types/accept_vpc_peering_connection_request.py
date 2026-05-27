"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcPeeringConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpc_peering_connection_id_with_resolver


class AcceptVpcPeeringConnectionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_id_with_resolver.VpcPeeringConnectionIdWithResolver"
    ]
    """<p>The ID of the VPC peering connection. You must specify this parameter in the request.</p>"""
