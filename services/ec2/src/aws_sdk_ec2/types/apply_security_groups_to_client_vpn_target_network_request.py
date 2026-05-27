"""Generated from Smithy shape ``com.amazonaws.ec2#ApplySecurityGroupsToClientVpnTargetNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.client_vpn_security_group_id_set
    import aws_sdk_ec2.types.vpc_id


class ApplySecurityGroupsToClientVpnTargetNetworkRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC in which the associated target network is located.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups to apply to the associated target network. Up to 5 security groups can be applied to an associated target network.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
