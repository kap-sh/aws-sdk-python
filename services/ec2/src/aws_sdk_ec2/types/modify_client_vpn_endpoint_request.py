"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyClientVpnEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_connect_options
    import aws_sdk_ec2.types.client_login_banner_options
    import aws_sdk_ec2.types.client_route_enforcement_options
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.client_vpn_security_group_id_set
    import aws_sdk_ec2.types.connection_log_options
    import aws_sdk_ec2.types.dns_servers_options_modify_structure
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.self_service_portal
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_configuration_input_structure
    import aws_sdk_ec2.types.vpc_id


class ModifyClientVpnEndpointRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint to modify.</p>"""
    server_certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the server certificate to be used. The server certificate must be provisioned in Certificate Manager (ACM).</p>"""
    connection_log_options: NotRequired[
        "aws_sdk_ec2.types.connection_log_options.ConnectionLogOptions"
    ]
    """<p>Information about the client connection logging options.</p> <p>If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:</p> <ul> <li> <p>Client connection requests</p> </li> <li> <p>Client connection results (successful and unsuccessful)</p> </li> <li> <p>Reasons for unsuccessful client connection requests</p> </li> <li> <p>Client connection termination time</p> </li> </ul>"""
    dns_servers: NotRequired[
        "aws_sdk_ec2.types.dns_servers_options_modify_structure.DnsServersOptionsModifyStructure"
    ]
    """<p>Information about the DNS servers to be used by Client VPN connections. A Client VPN endpoint can have up to two DNS servers.</p>"""
    vpn_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The port number to assign to the Client VPN endpoint for TCP and UDP traffic.</p> <p>Valid Values: <code>443</code> | <code>1194</code> </p> <p>Default Value: <code>443</code> </p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the Client VPN endpoint.</p>"""
    split_tunnel: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the VPN is split-tunnel.</p> <p>For information about split-tunnel VPN endpoints, see <a href=\"https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html\">Split-tunnel Client VPN endpoint</a> in the <i>Client VPN Administrator Guide</i>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of one or more security groups to apply to the target network.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC to associate with the Client VPN endpoint.</p>"""
    self_service_portal: NotRequired[
        "aws_sdk_ec2.types.self_service_portal.SelfServicePortal"
    ]
    """<p>Specify whether to enable the self-service portal for the Client VPN endpoint.</p>"""
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
    """<p>Indicates whether the client VPN session is disconnected after the maximum timeout specified in <code>sessionTimeoutHours</code> is reached. If <code>true</code>, users are prompted to reconnect client VPN. If <code>false</code>, client VPN attempts to reconnect automatically. The default value is <code>true</code>.</p>"""
    transit_gateway_configuration: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_configuration_input_structure.TransitGatewayConfigurationInputStructure"
    ]
    """<p>The Transit Gateway configuration for the Client VPN endpoint. This option is currently not supported.</p>"""
