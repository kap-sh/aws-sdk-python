"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskConfigurationListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_summary

OtaTaskConfigurationListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.ota_task_configuration_summary.OtaTaskConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskConfigurationListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.ota_task_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OtaTaskConfigurationListDefinition:
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_summary

    out: OtaTaskConfigurationListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.ota_task_configuration_summary.deserialize_json(
                item
            )
        )
    return out
