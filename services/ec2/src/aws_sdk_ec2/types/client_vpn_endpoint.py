"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_target_network_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_connect_response_options
    import aws_sdk_ec2.types.client_login_banner_response_options
    import aws_sdk_ec2.types.client_route_enforcement_response_options
    import aws_sdk_ec2.types.client_vpn_authentication_list
    import aws_sdk_ec2.types.client_vpn_endpoint_status
    import aws_sdk_ec2.types.client_vpn_security_group_id_set
    import aws_sdk_ec2.types.connection_log_response_options
    import aws_sdk_ec2.types.endpoint_ip_address_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.traffic_ip_address_type
    import aws_sdk_ec2.types.transit_gateway_configuration_describe_endpoint_structure
    import aws_sdk_ec2.types.transport_protocol
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpc_id
    import aws_sdk_ec2.types.vpn_protocol


class ClientVpnEndpoint(TypedDict):
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_status.ClientVpnEndpointStatus"
    ]
    """<p>The current state of the Client VPN endpoint.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the Client VPN endpoint was created.</p>"""
    deletion_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the Client VPN endpoint was deleted, if applicable.</p>"""
    dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name to be used by clients when connecting to the Client VPN endpoint.</p>"""
    client_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.</p>"""
    dns_servers: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>Information about the DNS servers to be used for DNS resolution. </p>"""
    split_tunnel: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether split-tunnel is enabled in the Client VPN endpoint.</p> <p>For information about split-tunnel VPN endpoints, see <a href=\"https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html\">Split-Tunnel Client VPN endpoint</a> in the <i>Client VPN Administrator Guide</i>.</p>"""
    vpn_protocol: NotRequired["aws_sdk_ec2.types.vpn_protocol.VpnProtocol"]
    """<p>The protocol used by the VPN session.</p>"""
    transport_protocol: NotRequired[
        "aws_sdk_ec2.types.transport_protocol.TransportProtocol"
    ]
    """<p>The transport protocol used by the Client VPN endpoint.</p>"""
    vpn_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The port number for the Client VPN endpoint.</p>"""
    associated_target_networks: NotRequired[
        "aws_sdk_ec2.types.associated_target_network_set.AssociatedTargetNetworkSet"
    ]
    """<p>Information about the associated target networks. A target network is a subnet in a VPC.</p>"""
    server_certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the server certificate.</p>"""
    authentication_options: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authentication_list.ClientVpnAuthenticationList"
    ]
    """<p>Information about the authentication method used by the Client VPN endpoint.</p>"""
    connection_log_options: NotRequired[
        "aws_sdk_ec2.types.connection_log_response_options.ConnectionLogResponseOptions"
    ]
    """<p>Information about the client connection logging options for the Client VPN endpoint.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Client VPN endpoint.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups for the target network.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    self_service_portal_url: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The URL of the self-service portal.</p>"""
    client_connect_options: NotRequired[
        "aws_sdk_ec2.types.client_connect_response_options.ClientConnectResponseOptions"
    ]
    """<p>The options for managing connection authorization for new client connections.</p>"""
    session_timeout_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum VPN session duration time in hours.</p> <p>Valid values: <code>8 | 10 | 12 | 24</code> </p> <p>Default value: <code>24</code> </p>"""
    client_login_banner_options: NotRequired[
        "aws_sdk_ec2.types.client_login_banner_response_options.ClientLoginBannerResponseOptions"
    ]
    """<p>Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.</p>"""
    client_route_enforcement_options: NotRequired[
        "aws_sdk_ec2.types.client_route_enforcement_response_options.ClientRouteEnforcementResponseOptions"
    ]
    """<p>Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.</p> <p>Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.</p>"""
    disconnect_on_session_timeout: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client VPN session is disconnected after the maximum <code>sessionTimeoutHours</code> is reached. If <code>true</code>, users are prompted to reconnect client VPN. If <code>false</code>, client VPN attempts to reconnect automatically. The default value is <code>true</code>.</p>"""
    endpoint_ip_address_type: NotRequired[
        "aws_sdk_ec2.types.endpoint_ip_address_type.EndpointIpAddressType"
    ]
    """<p>The IP address type of the Client VPN endpoint. Possible values are <code>ipv4</code> for IPv4 addressing only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack </code>for both IPv4 and IPv6 addressing.</p>"""
    traffic_ip_address_type: NotRequired[
        "aws_sdk_ec2.types.traffic_ip_address_type.TrafficIpAddressType"
    ]
    """<p>The IP address type of the Client VPN endpoint. Possible values are either <code>ipv4</code> for IPv4 addressing only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack</code> for both IPv4 and IPv6 addressing.</p>"""
    transit_gateway_configuration: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_configuration_describe_endpoint_structure.TransitGatewayConfigurationDescribeEndpointStructure"
    ]
    """<p>The Transit Gateway configuration for the Client VPN endpoint.</p>"""
