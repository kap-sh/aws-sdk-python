"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointConnectionNotificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_notification_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class ModifyVpcEndpointConnectionNotificationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    connection_notification_id: NotRequired[
        "aws_sdk_ec2.types.connection_notification_id.ConnectionNotificationId"
    ]
    """<p>The ID of the notification.</p>"""
    connection_notification_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN for the SNS topic for the notification.</p>"""
    connection_events: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The events for the endpoint. Valid values are <code>Accept</code>, <code>Connect</code>, <code>Delete</code>, and <code>Reject</code>.</p>"""
