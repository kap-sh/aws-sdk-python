"""Generated from Smithy shape ``com.amazonaws.ec2#PathRequestFilter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.request_filter_port_range


class PathRequestFilter(TypedDict):
    source_address: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The source IPv4 address.</p>"""
    source_port_range: NotRequired[
        "aws_sdk_ec2.types.request_filter_port_range.RequestFilterPortRange"
    ]
    """<p>The source port range.</p>"""
    destination_address: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The destination IPv4 address.</p>"""
    destination_port_range: NotRequired[
        "aws_sdk_ec2.types.request_filter_port_range.RequestFilterPortRange"
    ]
    """<p>The destination port range.</p>"""
