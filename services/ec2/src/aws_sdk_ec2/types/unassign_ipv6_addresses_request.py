"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignIpv6AddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.ipv6_address_list
    import aws_sdk_ec2.types.network_interface_id


class UnassignIpv6AddressesRequest(TypedDict):
    ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>The IPv6 prefixes to unassign from the network interface.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    ipv6_addresses: NotRequired["aws_sdk_ec2.types.ipv6_address_list.Ipv6AddressList"]
    """<p>The IPv6 addresses to unassign from the network interface.</p>"""
