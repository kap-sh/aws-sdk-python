"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.notification_configuration_structure

NotificationConfigurations: TypeAlias = list[
    "capo_notifications.types.notification_configuration_structure.NotificationConfigurationStructure"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfigurations) -> list:
    import capo_notifications.types.notification_configuration_structure

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.notification_configuration_structure.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NotificationConfigurations:
    import capo_notifications.types.notification_configuration_structure

    out: NotificationConfigurations = []
    for item in data:
        out.append(
            capo_notifications.types.notification_configuration_structure.deserialize_json(
                item
            )
        )
    return out
