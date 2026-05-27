"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogCloudWatchLogsDestination``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_delivery_status


class VerifiedAccessLogCloudWatchLogsDestination(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    delivery_status: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_delivery_status.VerifiedAccessLogDeliveryStatus"
    ]
    """<p>The delivery status for access logs.</p>"""
    log_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the CloudWatch Logs log group.</p>"""
