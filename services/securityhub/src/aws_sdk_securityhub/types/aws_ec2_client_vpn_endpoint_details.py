"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_list
    import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_details
    import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_login_banner_options_details
    import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_connection_log_options_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsEc2ClientVpnEndpointDetails(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the Client VPN endpoint. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A brief description of the endpoint. </p>"""
    client_cidr_block: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The IPv4 address range, in CIDR notation, from which client IP addresses are assigned. </p>"""
    dns_server: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> Information about the DNS servers to be used for DNS resolution. </p>"""
    split_tunnel: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether split-tunnel is enabled in the Client VPN endpoint. </p>"""
    transport_protocol: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The transport protocol used by the Client VPN endpoint. </p>"""
    vpn_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The port number for the Client VPN endpoint. </p>"""
    server_certificate_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the server certificate. </p>"""
    authentication_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_list.AwsEc2ClientVpnEndpointAuthenticationOptionsList"
    ]
    """<p> Information about the authentication method used by the Client VPN endpoint. </p>"""
    connection_log_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_connection_log_options_details.AwsEc2ClientVpnEndpointConnectionLogOptionsDetails"
    ]
    """<p> Information about the client connection logging options for the Client VPN endpoint. </p>"""
    security_group_id_set: NotRequired[
        "aws_sdk_securityhub.types.string_list.StringList"
    ]
    """<p> The IDs of the security groups for the target network. </p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the VPC. </p>"""
    self_service_portal_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The URL of the self-service portal. </p>"""
    client_connect_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_details.AwsEc2ClientVpnEndpointClientConnectOptionsDetails"
    ]
    """<p> The options for managing connection authorization for new client connections. </p>"""
    session_timeout_hours: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The maximum VPN session duration time in hours. </p>"""
    client_login_banner_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_login_banner_options_details.AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails"
    ]
    """<p> Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2ClientVpnEndpointDetails) -> dict:
    out: dict = {}
    if "client_vpn_endpoint_id" in value:
        out["ClientVpnEndpointId"] = value["client_vpn_endpoint_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_cidr_block" in value:
        out["ClientCidrBlock"] = value["client_cidr_block"]
    if "dns_server" in value:
        import aws_sdk_securityhub.types.string_list

        out["DnsServer"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["dns_server"]
        )
    if "split_tunnel" in value:
        out["SplitTunnel"] = value["split_tunnel"]
    if "transport_protocol" in value:
        out["TransportProtocol"] = value["transport_protocol"]
    if "vpn_port" in value:
        out["VpnPort"] = value["vpn_port"]
    if "server_certificate_arn" in value:
        out["ServerCertificateArn"] = value["server_certificate_arn"]
    if "authentication_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_list

        out["AuthenticationOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_list.serialize_json(
                value["authentication_options"]
            )
        )
    if "connection_log_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_connection_log_options_details

        out["ConnectionLogOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_connection_log_options_details.serialize_json(
                value["connection_log_options"]
            )
        )
    if "security_group_id_set" in value:
        import aws_sdk_securityhub.types.string_list

        out["SecurityGroupIdSet"] = (
            aws_sdk_securityhub.types.string_list.serialize_json(
                value["security_group_id_set"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "self_service_portal_url" in value:
        out["SelfServicePortalUrl"] = value["self_service_portal_url"]
    if "client_connect_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_details

        out["ClientConnectOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_details.serialize_json(
                value["client_connect_options"]
            )
        )
    if "session_timeout_hours" in value:
        out["SessionTimeoutHours"] = value["session_timeout_hours"]
    if "client_login_banner_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_login_banner_options_details

        out["ClientLoginBannerOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_login_banner_options_details.serialize_json(
                value["client_login_banner_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2ClientVpnEndpointDetails:
    out: AwsEc2ClientVpnEndpointDetails = {}  # type: ignore[typeddict-item]
    if "ClientVpnEndpointId" in data:
        out["client_vpn_endpoint_id"] = data["ClientVpnEndpointId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ClientCidrBlock" in data:
        out["client_cidr_block"] = data["ClientCidrBlock"]
    if "DnsServer" in data:
        import aws_sdk_securityhub.types.string_list

        out["dns_server"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["DnsServer"]
        )
    if "SplitTunnel" in data:
        out["split_tunnel"] = data["SplitTunnel"]
    if "TransportProtocol" in data:
        out["transport_protocol"] = data["TransportProtocol"]
    if "VpnPort" in data:
        out["vpn_port"] = data["VpnPort"]
    if "ServerCertificateArn" in data:
        out["server_certificate_arn"] = data["ServerCertificateArn"]
    if "AuthenticationOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_list

        out["authentication_options"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_list.deserialize_json(
                data["AuthenticationOptions"]
            )
        )
    if "ConnectionLogOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_connection_log_options_details

        out["connection_log_options"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_connection_log_options_details.deserialize_json(
                data["ConnectionLogOptions"]
            )
        )
    if "SecurityGroupIdSet" in data:
        import aws_sdk_securityhub.types.string_list

        out["security_group_id_set"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["SecurityGroupIdSet"]
            )
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SelfServicePortalUrl" in data:
        out["self_service_portal_url"] = data["SelfServicePortalUrl"]
    if "ClientConnectOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_details

        out["client_connect_options"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_details.deserialize_json(
                data["ClientConnectOptions"]
            )
        )
    if "SessionTimeoutHours" in data:
        out["session_timeout_hours"] = data["SessionTimeoutHours"]
    if "ClientLoginBannerOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_login_banner_options_details

        out["client_login_banner_options"] = (
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_client_login_banner_options_details.deserialize_json(
                data["ClientLoginBannerOptions"]
            )
        )
    return out
