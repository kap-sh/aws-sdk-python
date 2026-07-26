"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionSummariesListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.ota_task_execution_summaries

OtaTaskExecutionSummariesListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.ota_task_execution_summaries.OtaTaskExecutionSummaries"
]


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskExecutionSummariesListDefinition) -> list:
    import capo_iot_managed_integrations.types.ota_task_execution_summaries

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.ota_task_execution_summaries.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OtaTaskExecutionSummariesListDefinition:
    import capo_iot_managed_integrations.types.ota_task_execution_summaries

    out: OtaTaskExecutionSummariesListDefinition = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.ota_task_execution_summaries.deserialize_json(
                item
            )
        )
    return out
