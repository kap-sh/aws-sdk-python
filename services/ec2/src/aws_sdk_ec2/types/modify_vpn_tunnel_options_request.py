"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnTunnelOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_vpn_tunnel_options_specification
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_id


class ModifyVpnTunnelOptionsRequest(TypedDict):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the Amazon Web Services Site-to-Site VPN connection.</p>"""
    vpn_tunnel_outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    tunnel_options: NotRequired[
        "aws_sdk_ec2.types.modify_vpn_tunnel_options_specification.ModifyVpnTunnelOptionsSpecification"
    ]
    """<p>The tunnel options to modify.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    skip_tunnel_replacement: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Choose whether or not to trigger immediate tunnel replacement. This is only applicable when turning on or off <code>EnableTunnelLifecycleControl</code>.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    pre_shared_key_storage: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies the storage mode for the pre-shared key (PSK). Valid values are <code>Standard</code> (stored in Site-to-Site VPN service) or <code>SecretsManager</code> (stored in Amazon Web Services Secrets Manager).</p>"""
