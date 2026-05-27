"""Generated from Smithy shape ``com.amazonaws.ec2#AssignIpv6AddressesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.ipv6_address_list
    import aws_sdk_ec2.types.string


class AssignIpv6AddressesResult(TypedDict):
    assigned_ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The new IPv6 addresses assigned to the network interface. Existing IPv6 addresses that were assigned to the network interface before the request are not included.</p>"""
    assigned_ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>The IPv6 prefixes that are assigned to the network interface.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
