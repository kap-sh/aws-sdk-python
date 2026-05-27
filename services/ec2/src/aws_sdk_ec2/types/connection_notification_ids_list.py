"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotificationIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification_id

ConnectionNotificationIdsList: TypeAlias = list[
    "aws_sdk_ec2.types.connection_notification_id.ConnectionNotificationId"
]
