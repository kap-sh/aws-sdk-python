"""Generated from Smithy shape ``com.amazonaws.ec2#AssignIpv6AddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.ipv6_address_list
    import aws_sdk_ec2.types.network_interface_id


class AssignIpv6AddressesRequest(TypedDict):
    ipv6_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 prefixes that Amazon Web Services automatically assigns to the network interface. You cannot use this option if you use the <code>Ipv6Prefixes</code> option.</p>"""
    ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>One or more IPv6 prefixes assigned to the network interface. You can't use this option if you use the <code>Ipv6PrefixCount</code> option.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    ipv6_addresses: NotRequired["aws_sdk_ec2.types.ipv6_address_list.Ipv6AddressList"]
    """<p>The IPv6 addresses to be assigned to the network interface. You can't use this option if you're specifying a number of IPv6 addresses.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of additional IPv6 addresses to assign to the network interface. The specified number of IPv6 addresses are assigned in addition to the existing IPv6 addresses that are already assigned to the network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.</p>"""
