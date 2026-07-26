"""Generated from Smithy shape ``com.amazonaws.notifications#RegisterNotificationHubRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.region


class RegisterNotificationHubRequest(TypedDict, closed=True):
    notification_hub_region: "capo_notifications.types.region.Region"
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
