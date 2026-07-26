"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChannelAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_channel_association_summary

ManagedNotificationChannelAssociations: TypeAlias = list[
    "capo_notifications.types.managed_notification_channel_association_summary.ManagedNotificationChannelAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChannelAssociations) -> list:
    import capo_notifications.types.managed_notification_channel_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.managed_notification_channel_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedNotificationChannelAssociations:
    import capo_notifications.types.managed_notification_channel_association_summary

    out: ManagedNotificationChannelAssociations = []
    for item in data:
        out.append(
            capo_notifications.types.managed_notification_channel_association_summary.deserialize_json(
                item
            )
        )
    return out
