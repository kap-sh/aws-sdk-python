"""Generated from Smithy shape ``com.amazonaws.ec2#BaselineEbsBandwidthMbps``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class BaselineEbsBandwidthMbps(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum baseline bandwidth, in Mbps. If this parameter is not specified, there is no minimum limit.</p>"""
    max: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum baseline bandwidth, in Mbps. If this parameter is not specified, there is no maximum limit.</p>"""
