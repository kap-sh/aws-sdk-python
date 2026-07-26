"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportGeneratedCommands``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.matter_command_id

MatterCapabilityReportGeneratedCommands: TypeAlias = list[
    "capo_iot_managed_integrations.types.matter_command_id.MatterCommandId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportGeneratedCommands) -> list:
    return list(value)


def deserialize_json(data: list) -> MatterCapabilityReportGeneratedCommands:
    return list(data)
