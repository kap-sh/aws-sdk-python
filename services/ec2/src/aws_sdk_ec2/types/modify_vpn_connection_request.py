"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.customer_gateway_id
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.vpn_connection_id
    import aws_sdk_ec2.types.vpn_gateway_id


class ModifyVpnConnectionRequest(TypedDict):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the VPN connection.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    customer_gateway_id: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_id.CustomerGatewayId"
    ]
    """<p>The ID of the customer gateway at your end of the VPN connection.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.vpn_gateway_id.VpnGatewayId"]
    """<p>The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
