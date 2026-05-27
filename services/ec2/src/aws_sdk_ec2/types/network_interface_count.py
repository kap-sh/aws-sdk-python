"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceCount``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class NetworkInterfaceCount(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum number of network interfaces. If this parameter is not specified, there is no minimum limit.</p>"""
    max: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of network interfaces. If this parameter is not specified, there is no maximum limit.</p>"""
