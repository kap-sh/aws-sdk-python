"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceCountRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class NetworkInterfaceCountRequest(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum number of network interfaces. To specify no minimum limit, omit this parameter.</p>"""
    max: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of network interfaces. To specify no maximum limit, omit this parameter.</p>"""
