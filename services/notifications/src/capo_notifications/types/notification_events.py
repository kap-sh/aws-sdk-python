"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.notification_event_overview

NotificationEvents: TypeAlias = list[
    "capo_notifications.types.notification_event_overview.NotificationEventOverview"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationEvents) -> list:
    import capo_notifications.types.notification_event_overview

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.notification_event_overview.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationEvents:
    import capo_notifications.types.notification_event_overview

    out: NotificationEvents = []
    for item in data:
        out.append(
            capo_notifications.types.notification_event_overview.deserialize_json(item)
        )
    return out
