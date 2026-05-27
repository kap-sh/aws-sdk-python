"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesIpv6Address``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_address


class ScheduledInstancesIpv6Address(TypedDict):
    ipv6_address: NotRequired["aws_sdk_ec2.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address.</p>"""
