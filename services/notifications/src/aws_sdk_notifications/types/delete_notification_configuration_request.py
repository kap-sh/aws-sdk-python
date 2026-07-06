"""Generated from Smithy shape ``com.amazonaws.notifications#DeleteNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.notification_configuration_arn


class DeleteNotificationConfigurationRequest(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotificationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNotificationConfigurationRequest:
    out: DeleteNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
