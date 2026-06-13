"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_event_overview

ManagedNotificationEvents: TypeAlias = list[
    "aws_sdk_notifications.types.managed_notification_event_overview.ManagedNotificationEventOverview"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationEvents) -> list:
    import aws_sdk_notifications.types.managed_notification_event_overview

    out: list = []
    for item in value:
        out.append(
            aws_sdk_notifications.types.managed_notification_event_overview.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedNotificationEvents:
    import aws_sdk_notifications.types.managed_notification_event_overview

    out: ManagedNotificationEvents = []
    for item in data:
        out.append(
            aws_sdk_notifications.types.managed_notification_event_overview.deserialize_json(
                item
            )
        )
    return out
