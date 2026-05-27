"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrBlock``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Ipv6CidrBlock(TypedDict):
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
