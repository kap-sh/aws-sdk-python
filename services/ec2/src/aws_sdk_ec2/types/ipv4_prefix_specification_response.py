"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixSpecificationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Ipv4PrefixSpecificationResponse(TypedDict):
    ipv4_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 delegated prefixes assigned to the network interface.</p>"""
