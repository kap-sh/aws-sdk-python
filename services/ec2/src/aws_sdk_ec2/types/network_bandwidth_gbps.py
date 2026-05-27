"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkBandwidthGbps``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double


class NetworkBandwidthGbps(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The minimum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no minimum limit.</p>"""
    max: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The maximum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no maximum limit.</p>"""
