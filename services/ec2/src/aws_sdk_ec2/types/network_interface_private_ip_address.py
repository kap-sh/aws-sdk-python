"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePrivateIpAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_interface_association
    import aws_sdk_ec2.types.string


class NetworkInterfacePrivateIpAddress(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.network_interface_association.NetworkInterfaceAssociation"
    ]
    """<p>The association information for an Elastic IP address (IPv4) associated with the network interface.</p>"""
    primary: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this IPv4 address is the primary private IPv4 address of the network interface.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private DNS name.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IPv4 address.</p>"""
