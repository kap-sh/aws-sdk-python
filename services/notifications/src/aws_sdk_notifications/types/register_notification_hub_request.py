"""Generated from Smithy shape ``com.amazonaws.notifications#RegisterNotificationHubRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.region


class RegisterNotificationHubRequest(TypedDict):
    notification_hub_region: "aws_sdk_notifications.types.region.Region"
    """<p>The Region of the <code>NotificationHub</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterNotificationHubRequest) -> dict:
    out: dict = {}
    out["notificationHubRegion"] = value["notification_hub_region"]
    return out


def deserialize_json(data: dict) -> RegisterNotificationHubRequest:
    out: RegisterNotificationHubRequest = {}  # type: ignore[typeddict-item]
    if "notificationHubRegion" in data:
        out["notification_hub_region"] = data["notificationHubRegion"]
    else:
        raise DeserializationError(
            "RegisterNotificationHubRequest.notification_hub_region required"
        )
    return out
