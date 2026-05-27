"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignPrivateIpAddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_string_list


class UnassignPrivateIpAddressesRequest(TypedDict):
    ipv4_prefixes: NotRequired["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>The IPv4 prefixes to unassign from the network interface.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_string_list.PrivateIpAddressStringList"
    ]
    """<p>The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.</p>"""
