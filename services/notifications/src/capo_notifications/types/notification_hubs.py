"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationHubs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.notification_hub_overview

NotificationHubs: TypeAlias = list[
    "capo_notifications.types.notification_hub_overview.NotificationHubOverview"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationHubs) -> list:
    import capo_notifications.types.notification_hub_overview

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.notification_hub_overview.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationHubs:
    import capo_notifications.types.notification_hub_overview

    out: NotificationHubs = []
    for item in data:
        out.append(
            capo_notifications.types.notification_hub_overview.deserialize_json(item)
        )
    return out
