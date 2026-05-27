"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelLogOptionsSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cloud_watch_log_options_specification


class VpnTunnelLogOptionsSpecification(TypedDict):
    cloud_watch_log_options: NotRequired[
        "aws_sdk_ec2.types.cloud_watch_log_options_specification.CloudWatchLogOptionsSpecification"
    ]
    """<p>Options for sending VPN tunnel logs to CloudWatch.</p>"""
