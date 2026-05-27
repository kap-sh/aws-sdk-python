"""Generated from Smithy shape ``com.amazonaws.ec2#CreateClientVpnEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_connect_options
    import aws_sdk_ec2.types.client_login_banner_options
    import aws_sdk_ec2.types.client_route_enforcement_options
    import aws_sdk_ec2.types.client_vpn_authentication_request_list
    import aws_sdk_ec2.types.client_vpn_security_group_id_set
    import aws_sdk_ec2.types.connection_log_options
    import aws_sdk_ec2.types.endpoint_ip_address_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.self_service_portal
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.traffic_ip_address_type
    import aws_sdk_ec2.types.transit_gateway_configuration_input_structure
    import aws_sdk_ec2.types.transport_protocol
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpc_id


class CreateClientVpnEndpointRequest(TypedDict):
    client_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. Client CIDR range must have a size of at least /22 and must not be greater than /12.</p>"""
    server_certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the server certificate. For more information, see the <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/\">Certificate Manager User Guide</a>.</p>"""
    authentication_options: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authentication_request_list.ClientVpnAuthenticationRequestList"
    ]
    """<p>Information about the authentication method to be used to authenticate clients.</p>"""
    connection_log_options: NotRequired[
        "aws_sdk_ec2.types.connection_log_options.ConnectionLogOptions"
    ]
    """<p>Information about the client connection logging options.</p> <p>If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:</p> <ul> <li> <p>Client connection requests</p> </li> <li> <p>Client connection results (successful and unsuccessful)</p> </li> <li> <p>Reasons for unsuccessful client connection requests</p> </li> <li> <p>Client connection termination time</p> </li> </ul>"""
    dns_servers: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address configured on the device is used for the DNS server.</p>"""
    transport_protocol: NotRequired[
        "aws_sdk_ec2.types.transport_protocol.TransportProtocol"
    ]
    """<p>The transport protocol to be used by the VPN session.</p> <p>Default value: <code>udp</code> </p>"""
    vpn_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The port number to assign to the Client VPN endpoint for TCP and UDP traffic.</p> <p>Valid Values: <code>443</code> | <code>1194</code> </p> <p>Default Value: <code>443</code> </p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the Client VPN endpoint.</p>"""
    split_tunnel: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether split-tunnel is enabled on the Client VPN endpoint.</p> <p>By default, split-tunnel on a VPN endpoint is disabled.</p> <p>For information about split-tunnel VPN endpoints, see <a href=\"https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html\">Split-tunnel Client VPN endpoint</a> in the <i>Client VPN Administrator Guide</i>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Client VPN endpoint during creation.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of one or more security groups to apply to the target network. You must also specify the ID of the VPC that contains the security groups.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC to associate with the Client VPN endpoint. If no security group IDs are specified in the request, the default security group for the VPC is applied.</p>"""
    self_service_portal: NotRequired[
        "aws_sdk_ec2.types.self_service_portal.SelfServicePortal"
    ]
    """<p>Specify whether to enable the self-service portal for the Client VPN endpoint.</p> <p>Default Value: <code>enabled</code> </p>"""
    client_connect_options: NotRequired[
        "aws_sdk_ec2.types.client_connect_options.ClientConnectOptions"
    ]
    """<p>The options for managing connection authorization for new client connections.</p>"""
    session_timeout_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum VPN session duration time in hours.</p> <p>Valid values: <code>8 | 10 | 12 | 24</code> </p> <p>Default value: <code>24</code> </p>"""
    client_login_banner_options: NotRequired[
        "aws_sdk_ec2.types.client_login_banner_options.ClientLoginBannerOptions"
    ]
    """<p>Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.</p>"""
    client_route_enforcement_options: NotRequired[
        "aws_sdk_ec2.types.client_route_enforcement_options.ClientRouteEnforcementOptions"
    ]
    """<p>Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.</p> <p>Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.</p>"""
    disconnect_on_session_timeout: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client VPN session is disconnected after the maximum timeout specified in <code>SessionTimeoutHours</code> is reached. If <code>true</code>, users are prompted to reconnect client VPN. If <code>false</code>, client VPN attempts to reconnect automatically. The default value is <code>true</code>.</p>"""
    endpoint_ip_address_type: NotRequired[
        "aws_sdk_ec2.types.endpoint_ip_address_type.EndpointIpAddressType"
    ]
    """<p>The IP address type for the Client VPN endpoint. Valid values are <code>ipv4</code> (default) for IPv4 addressing only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack</code> for both IPv4 and IPv6 addressing. When set to <code>dual-stack,</code> clients can connect to the endpoint using either IPv4 or IPv6 addresses..</p>"""
    traffic_ip_address_type: NotRequired[
        "aws_sdk_ec2.types.traffic_ip_address_type.TrafficIpAddressType"
    ]
    """<p>The IP address type for traffic within the Client VPN tunnel. Valid values are <code>ipv4</code> (default) for IPv4 traffic only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack</code> for both IPv4 and IPv6 traffic. When set to <code>dual-stack</code>, clients can access both IPv4 and IPv6 resources through the VPN .</p>"""
    transit_gateway_configuration: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_configuration_input_structure.TransitGatewayConfigurationInputStructure"
    ]
    """<p>The Transit Gateway configuration for the Client VPN endpoint. Use this parameter to associate the endpoint with a Transit Gateway instead of a VPC. You cannot specify both <code>TransitGatewayConfiguration</code> and <code>VpcId</code>/<code>SecurityGroupIds</code>.</p>"""
