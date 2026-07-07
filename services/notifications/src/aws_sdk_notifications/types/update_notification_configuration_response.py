"""Generated from Smithy shape ``com.amazonaws.notifications#UpdateNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.notification_configuration_arn


class UpdateNotificationConfigurationResponse(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN used to update the <code>NotificationConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotificationConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UpdateNotificationConfigurationResponse:
    out: UpdateNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "UpdateNotificationConfigurationResponse.arn required"
        )
    return out
