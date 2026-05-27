"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionLogResponseOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ConnectionLogResponseOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether client connection logging is enabled for the Client VPN endpoint.</p>"""
    cloudwatch_log_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon CloudWatch Logs log group to which connection logging data is published.</p>"""
    cloudwatch_log_stream: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon CloudWatch Logs log stream to which connection logging data is published.</p>"""
