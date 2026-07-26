"""Generated from Smithy shape ``com.amazonaws.notifications#CreateNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.notification_configuration_status


class CreateNotificationConfigurationResponse(TypedDict, closed=True):
    arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>"""
    status: "capo_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
    """<p>The current status of this <code>NotificationConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CreateNotificationConfigurationResponse:
    out: CreateNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationResponse.arn required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationResponse.status required"
        )
    return out
