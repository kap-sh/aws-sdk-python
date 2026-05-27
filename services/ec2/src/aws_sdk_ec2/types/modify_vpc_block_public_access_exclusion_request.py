"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcBlockPublicAccessExclusionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.internet_gateway_exclusion_mode
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id


class ModifyVpcBlockPublicAccessExclusionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    exclusion_id: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
    ]
    """<p>The ID of an exclusion.</p>"""
    internet_gateway_exclusion_mode: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_exclusion_mode.InternetGatewayExclusionMode"
    ]
    """<p>The exclusion mode for internet gateway traffic.</p> <ul> <li> <p> <code>allow-bidirectional</code>: Allow all internet traffic to and from the excluded VPCs and subnets.</p> </li> <li> <p> <code>allow-egress</code>: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to Bidirectional.</p> </li> </ul>"""
