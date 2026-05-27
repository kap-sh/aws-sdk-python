"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PrefixSpecificationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Ipv6PrefixSpecificationResponse(TypedDict):
    ipv6_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 delegated prefixes assigned to the network interface.</p>"""
