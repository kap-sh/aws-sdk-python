"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChildEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_child_event_overview

ManagedNotificationChildEvents: TypeAlias = list[
    "capo_notifications.types.managed_notification_child_event_overview.ManagedNotificationChildEventOverview"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChildEvents) -> list:
    import capo_notifications.types.managed_notification_child_event_overview

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.managed_notification_child_event_overview.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedNotificationChildEvents:
    import capo_notifications.types.managed_notification_child_event_overview

    out: ManagedNotificationChildEvents = []
    for item in data:
        out.append(
            capo_notifications.types.managed_notification_child_event_overview.deserialize_json(
                item
            )
        )
    return out
