"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointConnectionNotificationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification
    import aws_sdk_ec2.types.string


class CreateVpcEndpointConnectionNotificationResult(TypedDict):
    connection_notification: NotRequired[
        "aws_sdk_ec2.types.connection_notification.ConnectionNotification"
    ]
    """<p>Information about the notification.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
