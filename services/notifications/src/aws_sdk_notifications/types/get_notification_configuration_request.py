"""Generated from Smithy shape ``com.amazonaws.notifications#GetNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.notification_configuration_arn


class GetNotificationConfigurationRequest(TypedDict):
    arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationRequest:
    out: GetNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
