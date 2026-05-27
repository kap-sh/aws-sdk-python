"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelLogOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cloud_watch_log_options


class VpnTunnelLogOptions(TypedDict):
    cloud_watch_log_options: NotRequired[
        "aws_sdk_ec2.types.cloud_watch_log_options.CloudWatchLogOptions"
    ]
    """<p>Options for sending VPN tunnel logs to CloudWatch.</p>"""
