"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceAwsLogsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ExpressGatewayServiceAwsLogsConfiguration(TypedDict):
    log_group: "aws_sdk_ecs.types.string.String"
    """<p>The name of the CloudWatch Logs log group to send container logs to.</p>"""
    log_stream_prefix: "aws_sdk_ecs.types.string.String"
    """<p>The prefix for the CloudWatch Logs log stream names. The default for an Express service is <code>ecs</code>.</p>"""
