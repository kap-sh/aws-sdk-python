"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportCommands``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.matter_command_id

MatterCapabilityReportCommands: TypeAlias = list[
    "capo_iot_managed_integrations.types.matter_command_id.MatterCommandId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportCommands) -> list:
    return list(value)


def deserialize_json(data: list) -> MatterCapabilityReportCommands:
    return list(data)
