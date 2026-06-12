"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#NotificationConfigurationListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.notification_configuration_summary

NotificationConfigurationListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.notification_configuration_summary.NotificationConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfigurationListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.notification_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.notification_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NotificationConfigurationListDefinition:
    import aws_sdk_iot_managed_integrations.types.notification_configuration_summary

    out: NotificationConfigurationListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.notification_configuration_summary.deserialize_json(
                item
            )
        )
    return out
