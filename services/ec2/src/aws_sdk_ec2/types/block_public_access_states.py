"""Generated from Smithy shape ``com.amazonaws.ec2#BlockPublicAccessStates``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_public_access_mode


class BlockPublicAccessStates(TypedDict):
    internet_gateway_block_mode: NotRequired[
        "aws_sdk_ec2.types.block_public_access_mode.BlockPublicAccessMode"
    ]
    """<p>The mode of VPC BPA.</p> <ul> <li> <p> <code>off</code>: VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.</p> </li> <li> <p> <code>block-bidirectional</code>: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).</p> </li> <li> <p> <code>block-ingress</code>: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.</p> </li> </ul>"""
