"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnection``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection_status
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class ClientVpnConnection(TypedDict):
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint to which the client is connected.</p>"""
    timestamp: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current date and time.</p>"""
    connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the client connection.</p>"""
    username: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The username of the client who established the client connection. This information is only provided if Active Directory client authentication is used.</p>"""
    connection_established_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the client connection was established.</p>"""
    ingress_bytes: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The number of bytes sent by the client.</p>"""
    egress_bytes: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The number of bytes received by the client.</p>"""
    ingress_packets: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The number of packets sent by the client.</p>"""
    egress_packets: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The number of packets received by the client.</p>"""
    client_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address of the client.</p>"""
    client_ipv6_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 address assigned to the client connection when using a dual-stack Client VPN endpoint. This field is only populated when the endpoint is configured for dual-stack addressing, and the client is using IPv6 for connectivity.</p>"""
    common_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The common name associated with the client. This is either the name of the client certificate, or the Active Directory user name.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>The current state of the client connection.</p>"""
    connection_end_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the client connection was terminated.</p>"""
    posture_compliance_statuses: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The statuses returned by the client connect handler for posture compliance, if applicable.</p>"""
