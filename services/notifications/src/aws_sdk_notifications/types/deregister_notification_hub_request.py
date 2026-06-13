"""Generated from Smithy shape ``com.amazonaws.notifications#DeregisterNotificationHubRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.region


class DeregisterNotificationHubRequest(TypedDict):
    notification_hub_region: "aws_sdk_notifications.types.region.Region"
    """<p>The <code>NotificationConfiguration</code> Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterNotificationHubRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterNotificationHubRequest:
    out: DeregisterNotificationHubRequest = {}  # type: ignore[typeddict-item]
    return out
