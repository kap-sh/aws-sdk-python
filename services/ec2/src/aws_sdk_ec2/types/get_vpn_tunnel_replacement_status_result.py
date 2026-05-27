"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnTunnelReplacementStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway_id
    import aws_sdk_ec2.types.maintenance_details
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.vpn_connection_id
    import aws_sdk_ec2.types.vpn_gateway_id


class GetVpnTunnelReplacementStatusResult(TypedDict):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the Site-to-Site VPN connection. </p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway associated with the VPN connection.</p>"""
    customer_gateway_id: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_id.CustomerGatewayId"
    ]
    """<p>The ID of the customer gateway.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.vpn_gateway_id.VpnGatewayId"]
    """<p>The ID of the virtual private gateway.</p>"""
    vpn_tunnel_outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    maintenance_details: NotRequired[
        "aws_sdk_ec2.types.maintenance_details.MaintenanceDetails"
    ]
    """<p>Get details of pending tunnel endpoint maintenance.</p>"""
