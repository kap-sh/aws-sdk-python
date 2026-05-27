"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignIpv6AddressesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.ipv6_address_list
    import aws_sdk_ec2.types.string


class UnassignIpv6AddressesResult(TypedDict):
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    unassigned_ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The IPv6 addresses that have been unassigned from the network interface.</p>"""
    unassigned_ipv6_prefixes: NotRequired[
        "aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"
    ]
    """<p>The IPv6 prefixes that have been unassigned from the network interface.</p>"""
