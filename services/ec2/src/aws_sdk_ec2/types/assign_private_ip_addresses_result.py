"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateIpAddressesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.assigned_private_ip_address_list
    import aws_sdk_ec2.types.ipv4_prefixes_list
    import aws_sdk_ec2.types.string


class AssignPrivateIpAddressesResult(TypedDict):
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    assigned_private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.assigned_private_ip_address_list.AssignedPrivateIpAddressList"
    ]
    """<p>The private IP addresses assigned to the network interface.</p>"""
    assigned_ipv4_prefixes: NotRequired[
        "aws_sdk_ec2.types.ipv4_prefixes_list.Ipv4PrefixesList"
    ]
    """<p>The IPv4 prefixes that are assigned to the network interface.</p>"""
