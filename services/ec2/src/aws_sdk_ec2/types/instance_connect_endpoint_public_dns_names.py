"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceConnectEndpointPublicDnsNames``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_connect_endpoint_dns_names


class InstanceConnectEndpointPublicDnsNames(TypedDict):
    ipv4: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_dns_names.InstanceConnectEndpointDnsNames"
    ]
    """<p>The IPv4-only DNS name of the EC2 Instance Connect Endpoint.</p>"""
    dualstack: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_dns_names.InstanceConnectEndpointDnsNames"
    ]
    """<p>The dualstack DNS name of the EC2 Instance Connect Endpoint. A dualstack DNS name supports connections from both IPv4 and IPv6 clients.</p>"""
