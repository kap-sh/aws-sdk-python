"""Generated from Smithy shape ``com.amazonaws.ec2#InstancePrivateIpAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_network_interface_association
    import aws_sdk_ec2.types.string


class InstancePrivateIpAddress(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_association.InstanceNetworkInterfaceAssociation"
    ]
    """<p>The association information for an Elastic IP address for the network interface.</p>"""
    primary: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this IPv4 address is the primary private IP address of the network interface.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IPv4 DNS name.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IPv4 address of the network interface.</p>"""
