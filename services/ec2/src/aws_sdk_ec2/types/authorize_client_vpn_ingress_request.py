"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeClientVpnIngressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.string


class AuthorizeClientVpnIngressRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    target_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the network for which access is being authorized.</p>"""
    access_group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the group to grant access to, for example, the Active Directory group or identity provider (IdP) group. Required if <code>AuthorizeAllGroups</code> is <code>false</code> or not specified.</p>"""
    authorize_all_groups: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to grant access to all clients. Specify <code>true</code> to grant all clients who successfully establish a VPN connection access to the network. Must be set to <code>true</code> if <code>AccessGroupId</code> is not specified.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the authorization rule.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
