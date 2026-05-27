"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolRange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class PublicIpv4PoolRange(TypedDict):
    first_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The first IP address in the range.</p>"""
    last_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The last IP address in the range.</p>"""
    address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of addresses in the range.</p>"""
    available_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of available addresses in the range.</p>"""
