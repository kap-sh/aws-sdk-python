"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionLogOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ConnectionLogOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether connection logging is enabled.</p>"""
    cloudwatch_log_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the CloudWatch Logs log group. Required if connection logging is enabled.</p>"""
    cloudwatch_log_stream: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the CloudWatch Logs log stream to which the connection data is published.</p>"""
