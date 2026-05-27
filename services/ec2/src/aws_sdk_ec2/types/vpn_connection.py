"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnection``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway_configuration
    import aws_sdk_ec2.types.gateway_association_state
    import aws_sdk_ec2.types.gateway_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vgw_telemetry_list
    import aws_sdk_ec2.types.vpn_connection_options
    import aws_sdk_ec2.types.vpn_state
    import aws_sdk_ec2.types.vpn_static_route_list


class VpnConnection(TypedDict):
    category: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The category of the VPN connection. A value of <code>VPN</code> indicates an Amazon Web Services VPN connection. A value of <code>VPN-Classic</code> indicates an Amazon Web Services Classic VPN connection.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway associated with the VPN connection.</p>"""
    vpn_concentrator_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPN concentrator associated with the VPN connection.</p>"""
    core_network_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the core network.</p>"""
    core_network_attachment_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the core network attachment.</p>"""
    gateway_association_state: NotRequired[
        "aws_sdk_ec2.types.gateway_association_state.GatewayAssociationState"
    ]
    """<p>The current state of the gateway association.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_options.VpnConnectionOptions"
    ]
    """<p>The VPN connection options.</p>"""
    routes: NotRequired["aws_sdk_ec2.types.vpn_static_route_list.VpnStaticRouteList"]
    """<p>The static routes associated with the VPN connection.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPN connection.</p>"""
    vgw_telemetry: NotRequired["aws_sdk_ec2.types.vgw_telemetry_list.VgwTelemetryList"]
    """<p>Information about the VPN tunnel.</p>"""
    pre_shared_key_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret storing the pre-shared key(s) for the VPN connection.</p>"""
    vpn_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPN connection.</p>"""
    state: NotRequired["aws_sdk_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the VPN connection.</p>"""
    customer_gateway_configuration: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_configuration.customerGatewayConfiguration"
    ]
    """<p>The configuration information for the VPN connection's customer gateway (in the native XML format). This element is always present in the <a>CreateVpnConnection</a> response; however, it's present in the <a>DescribeVpnConnections</a> response only if the VPN connection is in the <code>pending</code> or <code>available</code> state.</p>"""
    type: NotRequired["aws_sdk_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection.</p>"""
    customer_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the customer gateway at your end of the VPN connection.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.</p>"""
