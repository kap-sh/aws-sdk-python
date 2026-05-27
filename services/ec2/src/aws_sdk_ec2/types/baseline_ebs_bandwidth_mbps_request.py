"""Generated from Smithy shape ``com.amazonaws.ec2#BaselineEbsBandwidthMbpsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class BaselineEbsBandwidthMbpsRequest(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum baseline bandwidth, in Mbps. To specify no minimum limit, omit this parameter.</p>"""
    max: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum baseline bandwidth, in Mbps. To specify no maximum limit, omit this parameter.</p>"""
