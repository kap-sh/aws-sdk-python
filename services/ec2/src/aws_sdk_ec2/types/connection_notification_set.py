"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotificationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification

ConnectionNotificationSet: TypeAlias = list[
    "aws_sdk_ec2.types.connection_notification.ConnectionNotification"
]
