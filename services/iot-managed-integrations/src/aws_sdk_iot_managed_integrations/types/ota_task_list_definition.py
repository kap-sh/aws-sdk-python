"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_summary

OtaTaskListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.ota_task_summary.OtaTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.ota_task_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.ota_task_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OtaTaskListDefinition:
    import aws_sdk_iot_managed_integrations.types.ota_task_summary

    out: OtaTaskListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.ota_task_summary.deserialize_json(
                item
            )
        )
    return out
