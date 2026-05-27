"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateIpAddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_string_list


class AssignPrivateIpAddressesRequest(TypedDict):
    ipv4_prefixes: NotRequired["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>One or more IPv4 prefixes assigned to the network interface. You can't use this option if you use the <code>Ipv4PrefixCount</code> option.</p>"""
    ipv4_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv4 prefixes that Amazon Web Services automatically assigns to the network interface. You can't use this option if you use the <code>Ipv4 Prefixes</code> option.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_string_list.PrivateIpAddressStringList"
    ]
    """<p>The IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this parameter when also specifying a number of secondary IP addresses.</p> <p>If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.</p>"""
    secondary_private_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.</p>"""
    allow_reassignment: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.</p>"""
