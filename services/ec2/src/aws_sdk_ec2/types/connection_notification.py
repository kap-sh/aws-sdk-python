"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification_state
    import aws_sdk_ec2.types.connection_notification_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class ConnectionNotification(TypedDict):
    connection_notification_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the notification.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the endpoint service.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint.</p>"""
    connection_notification_type: NotRequired[
        "aws_sdk_ec2.types.connection_notification_type.ConnectionNotificationType"
    ]
    """<p>The type of notification.</p>"""
    connection_notification_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the SNS topic for the notification.</p>"""
    connection_events: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The events for the notification. Valid values are <code>Accept</code>, <code>Connect</code>, <code>Delete</code>, and <code>Reject</code>.</p>"""
    connection_notification_state: NotRequired[
        "aws_sdk_ec2.types.connection_notification_state.ConnectionNotificationState"
    ]
    """<p>The state of the notification.</p>"""
    service_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region for the endpoint service.</p>"""
