"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeClientVpnIngressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.string


class RevokeClientVpnIngressRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint with which the authorization rule is associated.</p>"""
    target_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the network for which access is being removed.</p>"""
    access_group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Active Directory group for which to revoke access. </p>"""
    revoke_all_groups: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether access should be revoked for all groups for a single <code>TargetNetworkCidr</code> that earlier authorized ingress for all groups using <code>AuthorizeAllGroups</code>. This does not impact other authorization rules that allowed ingress to the same <code>TargetNetworkCidr</code> with a specific <code>AccessGroupId</code>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
