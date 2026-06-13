"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_configuration_structure

ManagedNotificationConfigurations: TypeAlias = list[
    "aws_sdk_notifications.types.managed_notification_configuration_structure.ManagedNotificationConfigurationStructure"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationConfigurations) -> list:
    import aws_sdk_notifications.types.managed_notification_configuration_structure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_notifications.types.managed_notification_configuration_structure.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedNotificationConfigurations:
    import aws_sdk_notifications.types.managed_notification_configuration_structure

    out: ManagedNotificationConfigurations = []
    for item in data:
        out.append(
            aws_sdk_notifications.types.managed_notification_configuration_structure.deserialize_json(
                item
            )
        )
    return out
