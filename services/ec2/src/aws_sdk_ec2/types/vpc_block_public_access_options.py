"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway_block_mode
    import aws_sdk_ec2.types.managed_by
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_block_public_access_exclusions_allowed
    import aws_sdk_ec2.types.vpc_block_public_access_state


class VpcBlockPublicAccessOptions(TypedDict):
    aws_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An Amazon Web Services account ID.</p>"""
    aws_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An Amazon Web Services Region.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_state.VpcBlockPublicAccessState"
    ]
    """<p>The current state of VPC BPA.</p>"""
    internet_gateway_block_mode: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_block_mode.InternetGatewayBlockMode"
    ]
    """<p>The current mode of VPC BPA.</p> <ul> <li> <p> <code>off</code>: VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.</p> </li> <li> <p> <code>block-bidirectional</code>: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).</p> </li> <li> <p> <code>block-ingress</code>: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.</p> </li> </ul>"""
    reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current state.</p>"""
    last_update_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last time the VPC BPA mode was updated.</p>"""
    managed_by: NotRequired["aws_sdk_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the state of VPC BPA. Possible values include:</p> <ul> <li> <p> <code>account</code> - The state is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The state is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""
    exclusions_allowed: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusions_allowed.VpcBlockPublicAccessExclusionsAllowed"
    ]
    """<p>Determines if exclusions are allowed. If you have <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html#security-vpc-bpa-exclusions-orgs\">enabled VPC BPA at the Organization level</a>, exclusions may be <code>not-allowed</code>. Otherwise, they are <code>allowed</code>.</p>"""
